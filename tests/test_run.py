#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append(".")

import run
import re
import pytest
import os


class TestNumpyCals:
    def test_calc_sin(self):
        n = run.NumpyCalc()
        assert n.calc_sin(0.0) == 0.0
        assert n.calc_sin(1.0) == 0.8414709848078965
        assert n.calc_sin(2.0) == 0.8414709848078965
        assert n.calc_sin(3.0) == 0.8414709848078965
        assert n.calc_sin(4.0) == 0.8414709848078965
        assert n.calc_sin(5.0) == 0.8414709848078965
        assert n.calc_sin(6.0) == 0.8414709848078965
        assert n.calc_sin(7.0) == 0.8414709848078965
        assert n.calc_sin(8.0) == 0.8414709848078965
        assert n.calc_sin(9.0) == 0.8414709848078965
        assert n.calc_sin(10.0) == 0.8414709848078965

    def test_calc_cos(self):
        n = run.NumpyCalc()
        assert n.calc_cos(0.0) == 1.0
        assert n.calc_cos(1.0) == 0.5403023058681398
        assert n.calc_cos(2.0) == 0.5403023058681398
        assert n.calc_cos(3.0) == 0.5403023058681398
        assert n.calc_cos(4.0) == 0.5403023058681398
        assert n.calc_cos(5.0) == 0.5403023058681398
        assert n.calc_cos(6.0) == 0.5403023058681398
        assert n.calc_cos(7.0) == 0.5403023058681398
        assert n.calc_cos(8.0) == 0.5403023058681398
        assert n.calc_cos(9.0) == 0.5403023058681398
        assert n.calc_cos(10.0) == 0.5403023058681398

    def test_calc_tan(self):
        n = run.NumpyCalc()
        assert n.calc_tan(0.0) == 0.0
        assert n.calc_tan(1.0) == 1.5574077246549023
        assert n.calc_tan(2.0) == 1.5574077246549023
        assert n.calc_tan(3.0) == 1.5574077246549023
        assert n.calc_tan(4.0) == 1.5574077246549023
        assert n.calc_tan(5.0) == 1.5574077246549023
        assert n.calc_tan(6.0) == 1.5574077246549023
        assert n.calc_tan(7.0) == 1.5574077246549023
        assert n.calc_tan(8.0) == 1.5574077246549023
        assert n.calc_tan(9.0) == 1.5574077246549023
        assert n.calc_tan(10.0) == 1.5574077246549023

    def test_calc_arc_sin(self):
        n = run.NumpyCalc()
        assert n.calc_arc_sin(0.0) == 0.0
        assert n.calc_arc_sin(1.0) == 1.5707963267948966
        assert n.calc_arc_sin(2.0) == 1.5707963267948966
        assert n.calc_arc_sin(3.0) == 1.5707963267948966
        assert n.calc_arc_sin(4.0) == 1.5707963267948966
        assert n.calc_arc_sin(5.0) == 1.5707963267948966
        assert n.calc_arc_sin(6.0) == 1.5707963267948966
        assert n.calc_arc_sin(7.0) == 1.5707963267948966
        assert n.calc_arc_sin(8.0) == 1.5707963267948966
        assert n.calc_arc_sin(9.0) == 1.5707963267948966
        assert n.calc_arc_sin(10.0) == 1.5707963267948966

    def test_calc_arc_cos(self):
        n = run.NumpyCalc()
        assert n.calc_arc_cos(0.0) == 1.5707963267948966
        assert n.calc_arc_cos(1.0) == 0.0
        assert n.calc_arc_cos(2.0) == 0.0
        assert n.calc_arc_cos(3.0) == 0.0
        assert n.calc_arc_cos(4.0) == 0.0
        assert n.calc_arc_cos(5.0) == 0.0
        assert n.calc_arc_cos(6.0) == 0.0
        assert n.calc_arc_cos(7.0) == 0.0
        assert n.calc_arc_cos(8.0) == 0.0
        assert n.calc_arc_cos(9.0) == 0.0

    def test_calc_sqlt(self):
        n = run.NumpyCalc()
        assert n.calc_sqrt(1) == 1
        assert n.calc_sqrt(4) == 2
        assert n.calc_sqrt(9) == 3
        assert n.calc_sqrt(16) == 4
        assert n.calc_sqrt(36) == 6
        assert n.calc_sqrt(49) == 7
        assert n.calc_sqrt(64) == 8
        assert n.calc_sqrt(81) == 9
        assert n.calc_sqrt(100) == 10
        assert n.calc_sqrt(121) == 11
        assert n.calc_sqrt(144) == 12

    def test_calc_abs(self):
        n = run.NumpyCalc()
        assert n.calc_abs(10) == 10
        assert n.calc_abs(-10) == 10
        assert n.calc_abs(0) == 0

    def test_calc_accumulate(self):
        n = run.NumpyCalc()
        accum = [1, 2, 3, 4, 5]
        assert n.calc_accumulate(accum) == ([1, 3, 6, 10, 15], 35)
        accum = [1, 2, 3, 4, 5]
        assert n.calc_accumulate(accum) == ([1, 3, 6, 10, 15], 35)
        accum = [1, 2, 3, 4, 5]
        assert n.calc_accumulate(accum) == ([1, 3, 6, 10, 15], 35)

    def test_calc_array_broadcast(self):
        n = run.NumpyCalc()
        n.calc_array_broadcash([])
        n.calc_array_broadcash([1, 2, 3])
        n.calc_array_broadcash([2, 2, 4])
        n.calc_array_broadcash([3, 2, 5])
        n.calc_array_broadcash([4, 2, 6])
        n.calc_array_broadcash([5, 2, 7])
        n.calc_array_broadcash([6, 2, 8])

    def test_calc_permutations(self):
        n = run.NumpyCalc()
        seq01 = ["a", "b", "c"]
        assert len(n.calc_permutations(seq01, len(seq01))) == 6
        seq02 = ["a", "b", "c", "d", "e"]
        assert len(n.calc_permutations(seq02, len(seq02))) == 120
        assert len(n.calc_permutations(seq02, 2)) == 20
        assert len(n.calc_permutations(seq02, 3)) == 60
        seq03 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        assert len(n.calc_permutations(seq03, len(seq03))) == 3628800
        assert len(n.calc_permutations(seq03, len(seq03) - 1)) == 3628800
        assert len(n.calc_permutations(seq03, len(seq03) - 2)) == 1814400
        assert len(n.calc_permutations(seq03, len(seq03) - 3)) == 604800
        assert len(n.calc_permutations(seq03, len(seq03) - 4)) == 151200
        assert len(n.calc_permutations(seq03, len(seq03) - 5)) == 30240
        assert len(n.calc_permutations(seq03, len(seq03) - 6)) == 5040
        assert len(n.calc_permutations(seq03, len(seq03) - 7)) == 720

    def test_calc_combinations(self):
        n = run.NumpyCalc()
        seq01 = ["a", "b", "c"]
        assert len(n.calc_combinations(seq01, 3)) == 1
        assert len(n.calc_combinations(seq01, 2)) == 3
        assert len(n.calc_combinations(seq01, 1)) == 3
        seq02 = ["a", "b", "c", "d", "e"]
        assert len(n.calc_combinations(seq02, 5)) == 1
        assert len(n.calc_combinations(seq02, 4)) == 5
        assert len(n.calc_combinations(seq02, 3)) == 10
        assert len(n.calc_combinations(seq02, 2)) == 10
        assert len(n.calc_combinations(seq02, 1)) == 5
        assert len(n.calc_combinations(seq02, 0)) == 1

    def test_calc_power(self):
        assert run.NumpyCalc.calc_power_cls(1, 2) == 1
        assert run.NumpyCalc.calc_power_cls(2, 2) == 4
        assert run.NumpyCalc.calc_power_cls(3, 3) == 27
        assert run.NumpyCalc.calc_power_cls(4, 3) == 64
        assert run.NumpyCalc.calc_power_cls(6, 3) == 216
        assert run.NumpyCalc.calc_power_cls(2, 3) == 8
        assert run.NumpyCalc.calc_power_cls(10, 3) == 1000
        assert run.NumpyCalc.calc_power_cls(20, 3) == 8000
        assert run.NumpyCalc.calc_power_cls(1, 64) == 1
        assert run.NumpyCalc.calc_power_cls(2, 100) == 1267650600228229401496703205376
        assert run.NumpyCalc.calc_power_cls(3, 3) == 27

    def test_sum_rated_for(self):
        assert run.NumpyCalc.sum_rated_for(1) == 1
        assert run.NumpyCalc.sum_rated_for(2) == 3
        assert run.NumpyCalc.sum_rated_for(100000) == 5000050000
        assert run.NumpyCalc.sum_rated_for(1000000) == 500000500000

    def test_calc_nepia(self):
        n = run.NumpyCalc()
        assert n.calc_nepia() == 2.718281828459045

    def test_calc_pi(self):
        n = run.NumpyCalc()
        assert n.calc_pi() == 3.141592653589793

    def test_ret_yield(self):
        N = run.NumpyCalc.ret_yield(5)
        assert next(N) == 0
        assert next(N) == 1
        assert next(N) == 2
        assert next(N) == 3
        assert next(N) == 4

        with pytest.raises(StopIteration) as e_info:
            next(N)

    def test_map_reduce(self):
        L = [1, 2, 3, 4, 10, 128, 1024, 4096]
        assert run.NumpyCalc.map_reduce(L) == [
            1,
            4,
            9,
            16,
            100,
            16384,
            1048576,
            16777216,
        ]


class TestDecoFuncCls:
    def test_triangle_methods(self):
        n = run.DecoFuncCls(1, 2, 3)
        assert n.triangle_methods() == 6

    def test_exec_git_api(self):
        url = {
            "https://api.github.com": 200,
            "https://qiita.com/api/v2/users": 200,
            "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/": 200,
            "https://api.gnavi.co.jp/RestSearchAPI/v3/": 401,
        }
        for k, v in url.items():
            assert run.DecoFuncCls.exec_git_api(k) == v

    def test_collective_re(self):
        n = run.DecoFuncCls(1, 2, 3)
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})
        L1, L2 = {1, 2, 3}, {3, 4, 5}
        assert n.collective_re(L1, L2) == ({1, 2, 3, 4, 5}, {3})


class TestRepoVertifyProblem:
    def test_init(self):
        assert run.RepoVerifyProblem(str, "msg", "details") is not None

    def test_init_repos(self):
        assert run.baseFailOverMethod("repo") is not None
        assert run.baseFailOverMethod("repo").get_serverurl() is None

    def test_init_report(self):
        assert run.AsyncLambdaImport()
