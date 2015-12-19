#!/usr/bin/python
'''
Advent of Code 2015
Day 9

By Tyrus Tenneson
2015-12-17
'''
from collections import defaultdict
import copy
import os
import re
import sys

LINE_RE = re.compile(r'(\w*) to (\w*) = (\d*)')

def brute_tsp(current, remaining, from_to_dist, init=float('inf'), fun=min):
    if not remaining:
        return 0
    best = init
    for idx, nxt in enumerate(remaining):
        dist = from_to_dist[current][nxt]
        if dist == float('inf'):
            continue
        best = fun(best,
                   dist + brute_tsp(nxt, remaining[:idx] + remaining[idx + 1:],
                                    from_to_dist, init, fun))
    return best


def solve_one(problem):
    cities = problem.keys()
    problem['__start'] = defaultdict(int)
    answer = brute_tsp('__start', cities, problem)
    return answer


def solve_two(problem):
    cities = problem.keys()
    problem['__start'] = defaultdict(int)
    answer = brute_tsp('__start', cities, problem, init=float('-inf'), fun=max)
    return answer


def parse_problem(f):
    from_to_dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for line in f.readlines():
        c1, c2, distance = LINE_RE.match(line).groups()
        from_to_dist[c1][c2] = from_to_dist[c2][c1] = int(distance)
    return from_to_dist


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(copy.deepcopy(problem))
    print solve_two(copy.deepcopy(problem))


if __name__ == '__main__':
    print_solutions()
