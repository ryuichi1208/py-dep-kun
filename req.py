#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import collections
import functools
import asyncio
import aiohttp

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

