#!/usr/bin/env python3
"""A script to  Writing strings to Redis"""


import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional



def count_calls(method: Callable) -> Callable:
    """decorator takes a single method Callable
    argument and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # get the function name from the wrapped function
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """A Cache class that stores data in Redis."""

    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes, int, float]:
        """convert the data back to the desired format"""

        data = self._redis.get(key)
        if fn:
            return fn(data) if data else None
        else:
            return data

    def get_str(self, key: str):
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return self._redis.get(key, lambda x: x.decode("utf-8"))


    def get_int(self, key: str):
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return self._redis.get(key, int)
