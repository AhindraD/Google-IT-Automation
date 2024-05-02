# rearrange.py
#!/usr/bin/env python3

import unittest
import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


# ------------------xx--------------------xx------------------xx--------------------xx


# rearrange_test.py
#!/usr/bin/env python3

class TestRearrange(unittest.TestCase):

    def test_basic(self):  # basic case
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):  # edge case
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    
    def test_double_name(self):  # edge case    
        testcase = "Hopper, Grace M."
        excepted = "Grace M. Hopper"   
        self.assertEqual(rearrange_name(testcase), excepted)

    def test_one_name(self):  # edge case
        testcase = "Monty"
        excepted = "Monty"
        self.assertEqual(rearrange_name(testcase), excepted)


# Run the tests
unittest.main()


# chmod + x rearrange_test.py
# ./rearrange_test.py
