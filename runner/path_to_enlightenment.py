#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions to load the test cases ("koans") that make up the
Path to Enlightenment.
"""

import io
import unittest
import os
import sys


# The path to enlightenment starts with the following:
KOANS_FILENAME = "koans.txt"


def filter_koan_names(lines):
    """
    Strips leading and trailing whitespace, then filters out blank
    lines and comment lines.
    """
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            continue
        if line:
            yield line
    return


def names_from_file(filename):
    """
    Opens the given ``filename`` and yields the fully-qualified names
    of TestCases found inside (one per line).
    """
    with io.open(filename, "rt", encoding="utf8") as names_file:
        for name in filter_koan_names(names_file):
            yield name
    return


def koans_suite(names):
    """
    Returns a ``TestSuite`` loaded with all tests found in the given
    ``names``, preserving the order in which they are found.
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    for name in names:
        try:
            suite.addTests(loader.loadTestsFromName(name))
        except Exception as e:
            print(f"Failed to load test case '{name}': {e}")
    return suite


def koans():
    """
    Returns a ``TestSuite`` loaded with all the koans (``TestCase``s)
    listed in ``filename``.
    """
    # user = "summerduck"
    user = input("Enter a user name: ")
    names = names_from_file(KOANS_FILENAME)
    if user:
        names = [name.replace("koans.", f"koans_{user}.") for name in names]
    return koans_suite(names)
