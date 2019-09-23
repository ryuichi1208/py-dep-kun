#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

import run
import re
import pytest
import os

class TestDecoFuncCls:
    def test_calc_reduce(self):
        n = run.MultiProcTools()
        assert n.calc_reduce(1) == 0
        assert n.calc_reduce(8) == 24
        assert n.calc_reduce(16) == 112
        assert n.calc_reduce(32) == 480
        assert n.calc_reduce(64) == 1984
        assert n.calc_reduce(128) == 8064
        assert n.calc_reduce(256) == 32512
        assert n.calc_reduce(512) == 130560
        assert n.calc_reduce(1024) == 523264
        assert n.calc_reduce(2048) == 2095104
        assert n.calc_reduce(4096) == 8384512
        assert n.calc_reduce(8192) == 33546240
        assert n.calc_reduce(65536) == 2147418112

    def test_class_override(self):
        n = run.OverrideMethods("variable", 1.0, "methods")
        n = run.OverrideMethods("variable", 2.0, "methods")
        n = run.OverrideMethods("variable", 3.0, "methods")
        n = run.OverrideMethods("variable", 4.0, "methods")
        n = run.OverrideMethods("variable", 5.0, "methods")
        n = run.OverrideMethods("variable", 6.0, "methods")
        n = run.OverrideMethods("variable", 7.0, "methods")
        n = run.OverrideMethods("variable", 8.0, "methods")
