import argparse
import asyncio
from time import perf_counter

import httpx


async def get_url(num_request):

    url = "http://127.0.0.1:80/get_url"
    json = {"short_url": "PIcFaE"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=json)

        # print(f'Status request {num_request} ->', response.status_code)
        # print('Data response', response.json())
    return response


async def main(n: int):
    start = perf_counter()

    tasks = [get_url(i) for i in range(n)]
    await asyncio.gather(*tasks)

    finish = perf_counter()
    print(f"Time elapsed: {finish - start:.2f} seconds")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Test script to lunch n requests asynchronously"
    )
    parser.add_argument(
        "-n",
        "--num_requests",
        type=int,
        default=2,
        help="request numbers (by default : 2)",
    )
    args = parser.parse_args()
    asyncio.run(main(args.num_requests))
