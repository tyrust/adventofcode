#!/usr/bin/python
'''
Advent of Code 2015
Day 10

By Tyrus Tenneson
2015-12-18
'''
import os
import sys


def solve_one(problem):
    iterations = 40
    string = problem
    for _ in xrange(iterations):
        new_string = ''
        counting, count = '', 0
        for digit in string:
            if digit == counting:
                count += 1
            else:
                new_string += '%d%s' % (count, counting) if count else ''
                counting = digit
                count = 1
        new_string += '%d%s' % (count, counting) if count else ''
        string = new_string
    return len(string)


def solve_two(problem):
    return 'desu'


def parse_problem(f):
    return f.readline().strip()


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
