import pytest
from src.utils.url_generator_algo import Url_generator_algo

def test_length_shortUrl():
    url_gen:str = Url_generator_algo(6)
    assert len(url_gen.get_random_url_base62()) == 6

def test_valid_shortUrl():
    url_gen:str = Url_generator_algo(6)
    url = url_gen.get_random_url_base62()

    assert url.isalnum() == True

def test_valid_shortUrl_2():
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    url_gen:str = Url_generator_algo(6)
    url = url_gen.get_random_url_base62()

    assert all(c in base62 for c in url) == True