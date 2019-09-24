#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import os
import sys
import requests
import functools

from itertools import accumulate, permutations, combinations
from typing import Generator
from multiprocessing import Pool
from functools import lru_cache

# Package meta-data.
NAME = "py-dep-kun"
URL = "https://github.com/ryucihi1208/py-dep-kub"
EMAIL = "ryucrosskey@gmail.com"
AUTHOR = "ryucih1208"
VERSION = "1.0.0"


def debug(p):
    print("before:")
    print(p.before)
    print("--")
    print("after:")
    print(p.after)
    print("--")
    print(p.match.groups())
    print("--")


class NumpyCalc(object):
    """
    A class to extend the numpy cli for utilities.
    """

    def __init__(self):
        pass

    def calc_sin(self, rad: int) -> float:
        """
        Calculation function of sin function
        """
        rad = rad if rad < 1 else 1
        return numpy.sin(rad)

    def calc_cos(self, rad: int) -> float:
        """
        Calculation function of cos function
        """
        rad = rad if rad < 1 else 1
        return numpy.cos(rad)

    def calc_tan(self, rad: int) -> float:
        """
        Calculation function of tan function
        """
        rad = rad if rad < 1 else 1
        return numpy.tan(rad)

    def calc_arc_sin(self, rad: int) -> float:
        """
        Calculation function of arc_sin function
        """
        rad = rad if rad < 1 else 1
        return numpy.arcsin(rad)

    def calc_arc_cos(self, rad: int) -> float:
        """
        Calculation function of arc_cos function
        """
        rad = rad if rad < 1 else 1
        return numpy.arccos(rad)

    def calc_radians(self, rad: int) -> float:
        """
        Calculation function of radians function
        """
        rad = rad if rad < 1 else 1
        return numpy.radians(rad)

    def calc_exp(self, num: int) -> float:
        """
        Calculation function of exp function
        """
        return numpy.exp(num)

    def calc_log(self, num: int) -> float:
        """
        Calculation function of log function
        """
        return numpy.log(num)

    def calc_sqrt(self, num: int) -> float:
        """
        Calculation function of sqrt function
        """
        return numpy.sqrt(num)

    def calc_abs(self, num: int) -> float:
        """
        Calculation function of abs function
        """
        return numpy.abs(num)

    def calc_nepia(self) -> float:
        """
        Calculation function of nepia function
        """
        return numpy.e

    def calc_pi(self) -> float:
        """
        Calculation function of pi function
        """
        return numpy.pi

    def calc_accumulate(self, accum: list) -> tuple:
        tmp = list(accumulate(accum))
        return tmp, sum(tmp)

    def calc_permutations(self, perm: list, num: int) -> list:
        return list(permutations(perm, num))

    def calc_combinations(self, comb: list, num: int) -> list:
        return list(combinations(comb, num))

    @classmethod
    def calc_power_cls(cls, num: int, que: int) -> float:
        if que < 1:
            return 0
        return num ** que

    @staticmethod
    def sum_rated_for(num: int) -> int:
        ans = 0
        num = num if num >= 1 else 1
        return sum([i for i in range(num + 1)])

    @staticmethod
    def ret_yield(num: int) -> Generator:
        for i in range(num):
            yield i

    @staticmethod
    def map_reduce(ls: list):
        return list(map(lambda x: x * x, ls))


class DecoFuncCls(object):
    def __init__(self, x, y, z=1):
        self.__x = x
        self.__y = y
        self.__z = z

    def triangle_methods(self):
        return self.__x * self.__y * self.__z

    @classmethod
    def cat_string(cls, cat_list: list):
        ans = ""
        for cat in cat_list:
            if isinstance(cat, str):
                ans += cat
            else:
                continue
        return ans

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def exec_git_api(url: str) -> int:
        r = requests.get(url)
        return r.status_code

    # @functools.lru_cache(maxsize=None)
    def collective_re(self, L1: set, L2: set) -> tuple:
        return L1 | L2, L1 & L2


class MultiProcTools(object):
    """
    A class that supports multi-process execution in python
    """

    @staticmethod
    def multi_proc_function(x: int):
        proc_list = [i for i in range(x) if i % 2 == 0]
        return sum(list(map(lambda x: x * 2, proc_list)))

    def calc_reduce(self, x: int) -> int:
        return self.multi_proc_function(x)

    def gen_circle_area_func(self, pi):
        def circle_area(radius):
            return pi * radius ** 2

        return circle_area


class OverrideMethods(object):
    """
    A class that overrides the basic special methods of python
    """

    def __init__(self, name: str, version: int, function: str):
        self.__package = name
        self.__version = version
        self.__functions = function

    def __str__(self) -> str:
        return f"{self.__package}:{self.__version}-{self.__functions}"

    def __cmp__(self, other):
        if other is None:
            return 1

            #  Not a PackageObject(), so do this ourselves the bad way:
            return cmp(self.name, other.name) or cmp(self.arch, other.arch)

    def getDiscNum(self):
        return None

    @staticmethod
    def function_not():
        print("No........authn...")
        pass


def auth_login(func, user_info: dict):
    """
    Function for performing login authentication.
    If authentication is not performed, an error function is called.
    """
    auth_list = {"admin": "admin", "test01": "password", "test02": "password"}
    try:
        for k in user_info.keys():
            if auth_list[k] == user_info[k]:
                print("Authentication succeeded")

                def auth_exec_func(*args, **kwags):
                    """
                    Path that is called when authentication is actually successful.
                    """
                    func(*args, **kwags)

            else:
                raise KeyError

            return auth_exec_func
    except KeyError:
        print("Certification failed")

        def auth_not_func(*args, **kargs):
            # Function to call when authentication fails
            OverrideMethods.function_not()

        return auth_not_func


def h(a, b=0):
    print("aaa")


@auth_login(h, {"admin": "admin"})
def run():
    print("a")


if __name__ == "__main__":
    pass
