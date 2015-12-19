#!/usr/bin/python
'''
Advent of Code 2015
Day 2

By Tyrus Tenneson
2015-12-14
'''
import os
import sys


def solve_one(problem):
    total = 0
    for dim in problem:
        l, w, h = tuple(sorted(dim))
        total += (3 * l * w) + (2 * l * h) + (2 * w * h)
    return total


def solve_two(problem):
    total = 0
    for dim in problem:
        l, w, h = tuple(sorted(dim))
        total += (2 * l) + (2 * w) + (l * w * h)
    return total


def parse_problem(f):
    return [map(int, l.split('x')) for l in f.readlines()]


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
