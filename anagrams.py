#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys
import cProfile
# import re
import pstats
from io import BytesIO as StringIO
from collections import defaultdict

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "dbmiddle"


# cProfile.run('re.compile("foo|bar")')

def profile(func):
    """A decorator that uses cProfile to profile a function"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner


def alphabetize(string):
    """Returns alphabetized version of the string"""
    string = ''.join(sorted(string))
    return string


@profile
def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = defaultdict(set)
    for word in words:
        anagrams[alphabetize(word)].add(word)
    # anagrams = defaultdict(set)
    # for word in words:
    #     anagrams[alphabetize(word)].add(word)
    # return anagrams
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
        for word in words:
            word = word.lower()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print("{} : {}".format(k, v))


if __name__ == "__main__":
    main(sys.argv[1:])
