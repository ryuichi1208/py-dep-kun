#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append(".")

import run
import re
import pytest
import os


@pytest.fixture
def class_init_fixture():
    send_msg_001 = "TestMessage"
    send_msg_002 = "TestMessage__"
    send_msg_003 = "__TestMessage"
    send_msg_004 = "TestMessage" * 1024
    send_msg_005 = None

    return run.MultiProcTools(), send_msg_001


class TestFixtureMethodTest(object):
    def test_calc_once(self, class_init_fixture):
        n, msg = class_init_fixture
        assert n.calc_reduce(1) == 0
        assert n.calc_reduce(8) == 24
        assert n.calc_reduce(16) == 112


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

    def test_gen_circle_area_func01(self):
        n = run.MultiProcTools()
        out_exec_functions = n.gen_circle_area_func(3.14)
        assert out_exec_functions(1) == 3.14
        assert out_exec_functions(2) == 12.56

    def test_gen_circle_area_func02(self):
        n = run.MultiProcTools()
        out_exec_functions = n.gen_circle_area_func(3.141592)
        assert out_exec_functions(1) == 3.141592
        assert out_exec_functions(2) == 12.566368


# label_lines = [line.rstrip() for line in tf.gfile.GFile('retrained_labels.txt')]
# with tf.gfile.FastGFile('retrained_graph.pb', 'rb') as f:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())
#     _ = tf.import_graph_def(graph_def, name='')


class TestCreateProc:
    def test_proc_create(self):
        n = run.ProccessCreateClass()
        n.proc_create(2, [1, 2, 3])
        n.proc_create(2, [1, 1, 1])
        n.proc_create(6, [1, 2, 3])
