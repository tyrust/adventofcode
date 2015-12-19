#!/usr/bin/python
'''
Advent of Code 2015
Day 10

By Tyrus Tenneson
2015-12-18
'''
import os
import sys


def solve(problem, iterations):
    iterations = iterations
    string = problem
    for idx in xrange(iterations):
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
    return string


def solve_one(problem):
    return solve(problem, 40)


def solve_two(problem):
    return solve(problem, 10)


def parse_problem(f):
    return f.readline().strip()


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    one = solve_one(problem)
    print len(one)
    # save some work
    print len(solve_two(one))


if __name__ == '__main__':
    print_solutions()
