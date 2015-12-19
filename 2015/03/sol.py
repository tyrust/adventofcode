#!/usr/bin/python
'''
Advent of Code 2015
Day 3

By Tyrus Tenneson
2015-12-14
'''
import os
import sys


def solve_one(problem):
    position = (0, 0)
    delta = {
        '^': (1, 0),
        '>': (0, 1),
        'v': (-1, 0),
        '<': (0, -1),
    }
    homes = set((position,))
    for direction in problem:
        position = tuple(map(sum, zip(position, delta[direction])))
        homes.add(position)
    return len(homes)


def solve_two(problem):
    positions = [(0, 0), (0, 0)]
    delta = {
        '^': (1, 0),
        '>': (0, 1),
        'v': (-1, 0),
        '<': (0, -1),
    }
    homes = set(positions)
    # Ah, good ol' unreadable list comprehensions.  Enjoy deciphering
    # this shit.
    direction_groups = [tuple(problem[i:i+2])
                        for i in xrange(0, len(problem), 2)]
    for directions in direction_groups:
        positions = map(lambda l: tuple(map(sum, zip(*l))),
                        zip(positions, [delta[d] for d in directions]))
        [homes.add(p) for p in positions]
    return len(homes)


def parse_problem(f):
    return f.read().strip()


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
