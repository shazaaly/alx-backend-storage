#!/usr/bin/env python3
"""A script to  Writing strings to Redis"""


import redis
import uuid
from typing import Union


class Cache:
    """A Cache class that stores data in Redis."""

    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""

        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str):
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return self._redis.get(key, int)
