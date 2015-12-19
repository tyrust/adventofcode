#!/usr/bin/python
'''
Advent of Code 2015
Day 8

By Tyrus Tenneson
2015-12-16
'''
import os
import re
import sys


def solve_one(problem):
    total = 0
    for literal in problem:
        # minus 2 for quotes
        total += len(literal) - (len(literal.decode('string-escape')) - 2)
    return total


def solve_two(problem):
    total = 0
    for literal in problem:
        # plus 2 for quotes
        total += len(re.escape(literal)) + 2 - len(literal)
    return total


def parse_problem(f):
    return [l.strip() for l in f.readlines()]


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
