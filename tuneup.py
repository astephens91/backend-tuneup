#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "astephens91 (Props to ZacharyKline for his work on Part B)"

import cProfile
import pstats
import functools
import timeit
import collections


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    functools.wraps(func)

    def deco_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('time')
        ps.print_stats()
        return result
    return deco_function


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = [item for item, count in collections.Counter(movies).items()
                  if count > 1]
    return duplicates


def timeit_helper(num_repeats, runs_per_repeat):
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup='from __main__ import find_duplicate_movies'
        )
    result = t.repeat(repeat=num_repeats, number=runs_per_repeat)
    per_call = min(result) / float(runs_per_repeat)
    print("Code executed {} times and repeated {}"
          .format(runs_per_repeat, num_repeats))
    print("Cumulative time cost: {:.4} seconds".format(result))
    print("Per call time cost  : {:.4} seconds".format(per_call))


def main():
    """Computes a list of duplicate movie entries"""
    # result = find_duplicate_movies('movies.txt')
    # print('Found {} duplicate movies:'.format(len(result)))
    # print('\n'.join(result))
    timeit_helper(3, 7)


if __name__ == '__main__':
    main()
