#!/usr/bin/python
'''
Advent of Code 2015
Day 13

By Tyrus Tenneson
2015-12-19
'''
from collections import defaultdict
import os
import re
import sys

LINE_RE = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next '
                     r'to (\w+).')
SIGN_FN = {
    'gain': lambda x: x,
    'lose': lambda x: -x,
}


def score(order, prefs):
    if len(order) == 1:
        # No order is terrible, we need to seat people.  This is
        # mostly just for the initial state of best in brute_force.
        return float('-inf')
    pairs = [(order[i], order[(i + 1) % len(order)])
             for i in xrange(len(order))]
    total = 0
    for p1, p2 in pairs:
        total += prefs[p1][p2] + prefs[p2][p1]
    return total


def brute_force(current, remaining, prefs):
    # n=7, this should be fiiiine.
    # If no one is left, seat them.
    if len(remaining) == 1:
        return remaining
    # Otherwise figure out who we should seat next.
    best = []
    for idx, person in enumerate(remaining):
        best = max(best,
                   [person] + brute_force(current + [person],
                                          remaining[:idx] + remaining[idx + 1:],
                                          prefs),
                   key=lambda order: score(current + order, prefs))
    return best


def solve_one(problem):
    best = brute_force([], problem.keys(), problem)
    return score(best, problem)


def solve_two(problem):
    for person in problem.keys():
        problem[person]['__me'] = 0
        problem['__me'][person] = 0
    best = brute_force([], problem.keys(), problem)
    return score(best, problem)


def parse_problem(f):
    problem = defaultdict(dict)
    for line in f.readlines():
        line = line.strip()
        p1, sign, delta, p2 = LINE_RE.match(line).groups()
        problem[p1][p2] = SIGN_FN[sign](int(delta))
    return problem


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
