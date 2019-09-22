#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import os
import sys
from typing import Generator


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
    def __init__(self):
        pass

    def calc_sin(self, rad: int) -> float:
        rad = rad if rad < 1 else 1
        return numpy.sin(rad)

    def calc_cos(self, rad: int) -> float:
        rad = rad if rad < 1 else 1
        return numpy.cos(rad)

    def calc_arc_sin(self, rad: int) -> float:
        rad = rad if rad < 1 else 1
        return numpy.arcsin(rad)

    def calc_arc_cos(self, rad: int) -> float:
        rad = rad if rad < 1 else 1
        return numpy.arccos(rad)

    def calc_radians(self, rad: int) -> float:
        rad = rad if rad < 1 else 1
        return numpy.radians(rad)

    def calc_exp(self, num: int) -> float:
        return numpy.exp(num)

    def calc_log(self, num: int) -> float:
        return numpy.log(num)

    def calc_sqrt(self, num: int) -> float:
        return numpy.sqrt(num)

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
