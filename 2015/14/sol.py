#!/usr/bin/python
'''
Advent of Code 2015
Day 14

By Tyrus Tenneson
2015-12-20
'''
import os
import re
import sys


LINE_RE = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then '
                     r'must rest for (\d+) seconds.')
TIME = 2503


def distance(time, speed, duration, cooldown):
    # First do full run-rest cycles.
    cycles, remaining = divmod(time, duration + cooldown)
    dist = cycles * speed * duration
    # Then run until out of time or deer juice.
    dist += speed * min(remaining, duration)
    return dist


def solve_one(problem):
    return max(map(lambda spec: distance(TIME, *spec), problem.values()))


def simulate(time, specs):
    # TIME=2503 and there are 9 reindeer, just do it.
    schedules = {deer: [spec[0]] * spec[1] + [0] * spec[2]
                        for deer, spec in specs.iteritems()}
    locations = {deer: 0 for deer in specs.keys()}
    scores = {deer: 0 for deer in specs.keys()}
    for second in xrange(TIME):
        for deer, schedule in schedules.iteritems():
            locations[deer] += schedule[second % len(schedule)]
        furthest = max(locations.values())
        for deer, location in locations.iteritems():
            if location == furthest:
                scores[deer] += 1
    return max(scores.values())


def solve_two(problem):
    return simulate(TIME, problem)


def parse_problem(f):
    problem = {}
    for line in f.readlines():
        line = line.strip()
        deer, speed, duration, cooldown = LINE_RE.match(line).groups()
        problem[deer] = tuple(map(int, (speed, duration, cooldown)))
    return problem


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
