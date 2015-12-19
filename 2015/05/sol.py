#!/usr/bin/python
'''
Advent of Code 2015
Day 5

By Tyrus Tenneson
2015-12-15
'''
import os
import sys


def solve_one(problem):
    nice = 0
    vowels = 'aeiou'
    naughty_groups = ['ab', 'cd', 'pq', 'xy']
    for string in problem:
        prev = 'xx'
        vowel_count = 0
        has_double = False
        has_naughty = False
        for char in string:
            if prev + char in naughty_groups:
                has_naughty = True
                break
            if char in vowels:
                vowel_count += 1
            if char == prev:
                has_double = True
            prev = char
        if not has_naughty and has_double and vowel_count >= 3:
            nice += 1
    return nice


# I did this in a really stupid way.
def solve_two(problem):
    nice = 0
    for string in problem:
        prevprev, prev = '', ''
        pairs = {}
        has_two_pairs = False
        has_sandwich = False
        for idx,char in enumerate(string):
            if prev + char in pairs:
                if pairs[prev+char] != idx-1:
                    has_two_pairs = True
            else:
                pairs[prev + char] = idx
            if char == prevprev:
                has_sandwich = True
                jeeze = prevprev+prev+char
            prevprev = prev
            prev = char
        if has_two_pairs and has_sandwich:
            nice += 1
    return nice


def parse_problem(f):
    return [l.strip() for l in f.readlines()]


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
