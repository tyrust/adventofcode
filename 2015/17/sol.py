#!/usr/bin/python
'''
Advent of Code 2015
Day 12

By Tyrus Tenneson
2015-12-19
'''
import os
import sys

def solve_one(problem):
    return problem


def solve_two(problem):
    return 'desu'


def parse_problem(f):
    return f


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
