#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json

host = "api.github.com"

def pre_http_exec(func):
    def wapper(*args, **kwargs):
        print(host)
        func(*args, **kwargs)
        print("02")
    return wapper

@pre_http_exec(host)
def exec_http_requests(url: str, headers: dict = {}, params: dict = {}):
    ret = requests.get(url)

def run():
    exec_http_requests("aaa")

if __name__ == "__main__":
    run()
