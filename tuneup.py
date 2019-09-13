#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "astephens91"

import cProfile
import pstats
import functools
import time
import timeit


def profile_timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()    # 1
        value = func(*args, **kwargs)
        end_time = time.time()      # 2
        run_time = end_time - start_time    # 3
        print("Finished {} in {:.4f} secs".format(func.__name__, run_time))
        return value
    return wrapper_timer


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper(num_repeats, runs_per_repeat):
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup='from __main__ import find_duplicate_movies'
        )
    result = t.repeat(repeat=num_repeats, number=runs_per_repeat)
    print("Code executed {} times and repeated {}"
          .format(runs_per_repeat, num_repeats))
    print("Cumulative time cost: {:.4} seconds".format(result))
    print("Per call time cost  : {:.4} seconds".format(len(result)/1000000))


def main():
    """Computes a list of duplicate movie entries"""
    # result = find_duplicate_movies('movies.txt')
    # print('Found {} duplicate movies:'.format(len(result)))
    # print('\n'.join(result))
    timeit_helper(1, 7)


if __name__ == '__main__':
    main()
