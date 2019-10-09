#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import collections
import functools
import asyncio
import aiohttp
import concurrent.futures
import math
import pickle
# from Crypto.Cipher import AES


@functools.singledispatch
def regist_functions(L):
    return L


@regist_functions.register(list)
def deque_pop(L: list) -> collections.deque:
    try:
        ret = collections.deque(L)
    except Exception:
        print("Not iterable")
    else:
        print("Iterable")

    print(ret)
    return ret if ret else None


@regist_functions.register(dict)
def deque_dict(L: dict) -> collections.defaultdict:
    print("dict")
    return collections.defaultdict(L)


async def coros(seconds: int, value: int):
    await asyncio.sleep(seconds)
    return value + 100


# create new invent loop
# asyncio.run(coros(2,100))
# print(10)


def gen_func1():
    for i in range(3):
        yield i


def gen_func2():
    for i in range(3):
        yield i


def gen_wrapper(gen_func1, gen_func2):
    yield from gen_func1()
    yield from gen_func2()
    yield from ["a", "b"]


# for i in gen_wrapper(gen_func1, gen_func2):
#     print(i)


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def process_create_function(n: list) -> bool:
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        for number, prime in zip(n, executor.map(is_prime, n)):
            print(f"{number} is prime")

# def do_encrypto(key: str, iv=b'0*'*16):
#     aes = AES.new(key, AES.MODE_CBC, iv)
#     cipher = aes.encrypt("python script000".encode("ascii"))
#     return cipher

class DefPrintMethod(object):
    """
     __class__
     __delattr__
     __dict__
     __dir__
     __doc__
     __eq__
     __format__
     __ge__
     __getattribute__
     __gt__
     __hash__
     __init__
     __init_subclass__
     __le__
     __lt__
     __module__
     __ne__
     __new__
     __reduce__
     __reduce_ex__
     __repr__
     __setattr__
     __sizeof__
     __str__
     __subclasshook__
     __weakref__
    """

    def create_pickle(self, obj, fd):
        if obj is not  None:
            pickle.dump(obj, fd)

    def load_picke(self, pickle_file: str):
        try:
            os.stat(pickle_file)
        except FileNotFoundError:
            return None

    def do_pickle_dump(self, obj:object, filename: str) -> int:
        try:
            with open(filename, "wb") as f:
                pickle.dump(obj, f)
            return 0
        except Exception:
            return 1
