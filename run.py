#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This program is a run package to check the basic operation of Python.
#

import numpy
import os
import sys
import re
import requests
import time
import functools
import logging

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

logging.basicConfig(level=logging.DEBUG)


class UpdateNojice(object):

    """
    A single update notice (for instance, a security fix).
    """

    def __init__(self, elem=None, repoid=None, vlogger=None):
        self._md = {
            "from": "",
            "type": "",
            "title": "",
            "release": "",
            "status": "",
            "version": "",
            "pushcount": "",
            "update_id": "",
            "issued": "",
            "updated": "",
            "description": "",
            "rights": "",
            "severity": "",
            "summary": "",
            "solution": "",
            "references": [],
            "pkglist": [],
            "reboot_suggested": False,
        }


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


class UpdateXmlModule(object):
    def __init__(self, repos=[], logger=None, vlogger=None):
        self._notices = {}
        self._cache = {}  # a pkg nvr => notice cache for quick lookups
        self._no_cache = {}  # a pkg name only => notice list
        self._repos = []  # list of repo ids that we've parsed

        self._logger = logger
        self._vlogger = vlogger


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


class baseFailOverMethod:
    """
    A base class to provide a failover to switch to a new server if
    the current one fails.
    """

    def __init__(self, repo):
        self.repo = repo
        self.failures = 0

    def get_serverurl(self, i=None):
        """
        Return a server URL based on this failover method, or None
        if there is a complete failure.  This method should always be
        used to translate an index into a URL, as this object may
        change how indexes map.
        """
        return None

    def server_failed(self):
        """
        Notify the failover method that the current server has
        failed.
        """
        self.failures = self.failures + 1

    def reset(self, i=0):
        """Reset the failures counter to the given index.
        :param i: the index to reset the failures counter to
        """
        self.failures = i

    def get_index(self):
        """
        Return the current number of failures, which is also the
        current index into the list of URLs that this object
        represents.
        """
        return self.failures

    def len(self):
        """
        Return the total number of URLs available to cycle through
        in this object.
        """
        return len(self.repo.urls)


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


def auth_login(auth_login_fun, user_info: dict):
    """
    Function for performing login authentication.
    If authentication is not performed, an error function is called.
    """
    print("ccc")
    auth_list = {"admin": "admin", "test01": "password", "test02": "password"}
    try:
        for k in user_info.keys():
            if auth_list[k] == user_info[k]:
                print("Authentication succeeded")

                def func(*args, **kwags):
                    """
                    Path that is called when authentication is actually successful.
                    """
                    print(auth_login_fun)
                    auth_login_fun(*args, **kwags)

            else:
                raise KeyError

            return auth_login_fun
    except KeyError:
        print("Certification failed")

        def auth_not_func(*args, **kargs):
            # Function to call when authentication fails
            OverrideMethods.function_not()

        return auth_not_func


def do_http_request_exeption(url: str = "localhost", port: int = 443):
    print(url, port)


@auth_login(do_http_request_exeption, {"admin": "admin"})
def target_auth_login():
    pass


class RepoVerifyProblem:
    """ Holder for each "problem" we find with a repo.verify(). """

    def __init__(self, type, msg, details, fake=False):
        self.type = type
        self.message = msg
        self.details = details
        self.fake = fake


if __name__ == "__main__":
    pass

PARSE_QUERY = """
select pkgKey from packages
where name %(op)s '%(q)s'
   or name || '.' || arch %(op)s '%(q)s'
   or name || '-' || version %(op)s '%(q)s'
   or name || '-' || version || '-' || release %(op)s '%(q)s'
   or name || '-' || version || '-' || release || '.' || arch %(op)s '%(q)s'
   or epoch || ':' || name || '-' || version || '-' || release || '.' || arch %(op)s '%(q)s'
   or name || '-' || epoch || ':' || version || '-' || release || '.' || arch %(op)s '%(q)s'
"""


_FULL_PARSE_QUERY_BEG = """
SELECT pkgId,pkgKey,name,epoch,version,release,arch,
  name || "." || arch AS sql_nameArch,
  name || "-" || version || "-" || release || "." || arch AS sql_nameVerRelArch,
  name || "-" || version AS sql_nameVer,
  name || "-" || version || "-" || release AS sql_nameVerRel,
  epoch || ":" || name || "-" || version || "-" || release || "." || arch AS sql_envra,
  name || "-" || epoch || ":" || version || "-" || release || "." || arch AS sql_nevra
  FROM packages
  WHERE
"""

class DevSecClass(object):
    """
    This class is a diffial use that inherits the base class.
    """
    def __init__(self):
        self.DSC_NUMBER = 20.0
        self.DSC_VERSION = "1.0.0"
        self.DSC_NAME = __name__
        self.DSC_DOC = __doc__
        self.DSC_AUTHO = None

    def ret_dir_functions(self):
        return tuple([d for d in tuple(dir(self))])

