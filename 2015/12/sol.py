#!/usr/bin/python
'''
Advent of Code 2015
Day 12

By Tyrus Tenneson
2015-12-19
'''
import json
import os
import sys

def solve_one(problem):
    if isinstance(problem, int):
        return problem
    elif isinstance(problem, dict):
        return sum(map(solve_one, problem.values()))
    elif isinstance(problem, list):
        return sum(map(solve_one, problem))
    return 0


def solve_two(problem):
    if isinstance(problem, int):
        return problem
    elif isinstance(problem, dict):
        if 'red' not in problem.values():
            return sum(map(solve_two, problem.values()))
    elif isinstance(problem, list):
        return sum(map(solve_two, problem))
    return 0


def parse_problem(f):
    return json.loads(f.readline())


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
