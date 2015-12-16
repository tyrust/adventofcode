#!/usr/bin/python
'''
Advent of Code 2015
Day 4

By Tyrus Tenneson
2015-12-14
'''
import hashlib
import os
import sys


def solve_one(problem):
    n = 0
    hash = '01234'
    while hash[:5] != '00000':
        n += 1
        hash = hashlib.md5(problem + str(n)).hexdigest()
    return n

def solve_two(problem):
    n = 0
    hash = '012345'
    while hash[:6] != '000000':
        n += 1
        hash = hashlib.md5(problem + str(n)).hexdigest()
    return n


def parse_problem(f):
    return f.read().strip()


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
