#!/usr/bin/env python3

# -------------------------------
# projects/idb/TestIDB.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase


# -----------
# TestIDB
# -----------

class TestIDB (TestCase) :

    # ----
    # read
    # ----

    def test_sample (self) :
        self.assertEqual(1, 1)

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestIDB.py >  TestIDB.out 2>&1



% coverage3 report -m                   >> TestIDB.out



% cat TestIDB.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
IDB          18      0      6      0   100%
TestIDB      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
