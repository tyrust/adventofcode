#!/usr/bin/python
'''
Advent of Code 2015
Day 1

By Tyrus Tenneson
2015-12-14
'''


def solve_one(problem):
    return sum([1 if c == '(' else -1 for c in problem])


def solve_two(problem):
    floor = 0
    for idx, c in enumerate(problem):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return idx + 1


def parse_problem(f):
    return f.read().strip()


def print_solutions():
    f = open('input', 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
