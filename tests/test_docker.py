#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os


def print_results(results):
    sorted(results.items(), key=lambda x: x[1])
    print("=======================")
    for dockerfile in results:
        print("{}: {}".format(dockerfile, results[dockerfile]))
    print("=======================")


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
