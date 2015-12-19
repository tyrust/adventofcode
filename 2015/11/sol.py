#!/usr/bin/python
'''
Advent of Code 2015
Day 11

By Tyrus Tenneson
2015-12-18
'''
import os
import sys


INVALID_LETTERS = 'ilo'
VALID_LETTERS = 'abcdefghjkmnpqrstuvwxyz'  # alpha - (i, l, o)
FUCK_IT = { 'i': 'j', 'l': 'm', 'o': 'p' }


def sanitize(password):
    new_password = password
    for idx, char in enumerate(password):
        if char in INVALID_LETTERS:
            new_password = (password[:idx] + FUCK_IT[char] +
                            'a' * (len(password) - idx - 1))
            break
    return new_password


def increment(password):
    new_password = password
    for idx, char in [x for x in enumerate(password)][::-1]:
        next_char = VALID_LETTERS[(VALID_LETTERS.index(char)
                                  + 1) % len(VALID_LETTERS)]
        new_password = new_password[:idx] + next_char + new_password[idx+1:]
        if next_char != 'a':
            break
    return new_password


def char_to_int(char):
    return int(char.encode('hex'), base=16)


def longest_straight(string):
    prev = 0
    curr, longest = 1, 0
    for char in string:
        if char_to_int(char) == prev + 1:
            curr += 1
        else:
            curr = 1
        longest = max(longest, curr)
        prev = char_to_int(char)
    return longest


def pair_count(string):
    prev = ''
    prev_pair_idx = -2  # start of previous pair
    count = 0
    for idx, char in enumerate(string):
        if char == prev and prev_pair_idx != idx - 2:
            count += 1
            prev_pair_idx = idx - 1
        prev = char
    return count


def solve_one(problem):
    password = sanitize(problem)
    checks = (
        lambda password: longest_straight(password) >= 3,
        # lambda password: all([c in VALID_LETTERS for c in password]),
        lambda password: pair_count(password) >= 2,
    )
    while True:
        password = increment(password)
        if all(map(lambda check: check(password), checks)):
            break
    return password


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
