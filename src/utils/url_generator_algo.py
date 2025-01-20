import random


class Url_generator_algo:
    """Generating a random string of length n using base62 characters"""

    def __init__(self, lenght: int):
        self.length: int = lenght

    def get_random_url_base62(self) -> str:
        base62: str = (
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        return "".join(random.choices(base62, k=self.length))

    def get_length(self) -> int:
        return self.length
