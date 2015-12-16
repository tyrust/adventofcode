#!/usr/bin/python
'''
Advent of Code 2015
Day 6

By Tyrus Tenneson
2015-12-15
'''
import os
import re
import sys

COMMAND_REGEX = re.compile(r'(?P<command>[^\d]+) (?P<c1>[^ ]+) through '
                           r'(?P<c2>.*)')
ON = 'turn on'
OFF = 'turn off'
TOGGLE = 'toggle'


class Grid:
    def __init__(self, size, command_map):
        self._state = [[0 for _ in range(size)] for _ in range(size)]
        self._command_map = command_map

    '''
    Go from c1 to c2, applying fun (a lambda) to each point.
    '''
    def _traverse(self, c1, c2, fun):
        x_range, y_range = map(sorted, zip(c1, c2))
        for x in xrange(x_range[0], x_range[1] + 1):
            for y in xrange(y_range[0], y_range[1] + 1):
                self._state[x][y] = fun(self._state[x][y])

    def execute(self, request):
        command, c1, c2 = request
        self._traverse(c1, c2, self._command_map[command])

    def count_on(self):
        return sum(map(sum, self._state))

    def __str__(self):
        return '\n'.join([''.join(map(str, l)) for l in self._state])


def solve_one(problem):
    command_map = {
        ON: lambda p: 1,
        OFF: lambda p: 0,
        TOGGLE: lambda p: p ^ 1,
    }
    grid = Grid(1000, command_map)
    for request in problem:
        grid.execute(request)
    return grid.count_on()


def solve_two(problem):
    command_map = {
        ON: lambda p: p + 1,
        OFF: lambda p: max(p - 1, 0),
        TOGGLE: lambda p: p + 2,
    }
    grid = Grid(1000, command_map)
    for request in problem:
        grid.execute(request)
    return grid.count_on()


def parse_problem(f):
    problem = []
    for l in f.readlines():
        matches = COMMAND_REGEX.match(l).groupdict()
        problem.append((matches['command'],
                        tuple(map(int, matches['c1'].split(','))),
                        tuple(map(int, matches['c2'].split(',')))))
    return tuple(problem)


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
