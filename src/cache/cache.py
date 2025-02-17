import hashlib
import json

from redis.asyncio import Redis
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, StreamingResponse

from src.config import logger, settings
from src.utils.timer import measure_time


class CacheMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.cache_enabled = settings.cache_enabled
        self.redis_client = Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
        )

    async def log(self, message):
        logger.info(message)

    @measure_time
    async def dispatch(self, request, call_next):

        await self.log("middleware start")

        includ_paths = ["/get_url"]

        if not self.cache_enabled or request.url.path not in includ_paths:

            await self.log("Cache disabled")
            return await call_next(request)

        # Generate a cache key based on the request path and query parameters

        body = await request.body()

        body_data = json.loads(body.decode("utf-8"))
        url_path, query_params = request.url.path, body_data
        cache_key = self._generate_cache_key(url_path, query_params)

        try:
            cached_response = await self.redis_client.get(cache_key)
            if cached_response:

                await self.log("Cache HIT")

                return Response(
                    content=cached_response,
                    media_type="application/json",
                    headers={"X-Cache": "HIT"},
                )

        except Exception as e:
            await self.log(f"Redis error during request redis: {e}")

        # next request in the middleware stack
        response = await call_next(request)

        # process the streaming response
        if (
            isinstance(response, (StreamingResponse,))
            or type(response).__name__ == "_StreamingResponse"
        ):
            content = b""
            async for chunk in response.body_iterator:
                content += chunk
            response = Response(
                content=content,
                status_code=response.status_code,
                headers=dict(response.headers),
            )

        try:
            if response.status_code == 200:
                await self.redis_client.set(
                    cache_key, response.body, ex=settings.cache_expire
                )
                await self.log("Put in cache")
        except Exception as e:
            await self.log(f"Redis error during writting on cache: {e}")
        return response

    def _generate_cache_key(self, path: str, query_params: dict) -> str:
        """
        Generate unique cache key based on
        the request path and query parameters
        """
        raw_key = f"{path}?{query_params}"
        return hashlib.sha256(raw_key.encode()).hexdigest()
