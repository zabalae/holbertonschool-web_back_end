#!/usr/bin/env python3
'''Redis Basic'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method Callable argument
    and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments the count for that key every time the method
        is called and returns the value returned by the original method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """saves the input and output of each function in redis
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        output = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper

class Cache():
    """Cache class with redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Callable = None):
        """
        Take a key string argument and an optional Callable 
        argument and convert the data back to the desired format
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            if fn is int:
                raise ValueError("Can not use 'int' callable for this key.")
            try:
                return fn(data)
            except Exception as e:
                return str(e)
        return data

    def get_str(self, key: str):
        """get_str method"""
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str):
        """get_int method"""
        return self.get(key, fn=int)

    def get_call_count(self, method_name: str):
        """get_call_count method"""
        count_key = f"call_count:{method_name}"
        count = self._redis.get(count_key)
        return int(count) if count is not None else 0
    
def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')
