#!/usr/bin/python
'''
Advent of Code 2015
Day 2

By Tyrus Tenneson
2015-12-14
'''


def solve_one(input):
    total = 0
    for dim in input:
        l, w, h = tuple(sorted(dim))
        total += (3 * l * w) + (2 * l * h) + (2 * w * h)
    return total


def solve_two(input):
    total = 0
    for dim in input:
        l, w, h = tuple(sorted(dim))
        total += (2 * l) + (2 * w) + (l * w * h)
    return total


def parse_input(file):
    return [map(int, l.split('x')) for l in file.readlines()]


if __name__ == '__main__':
    file = open('input', 'r')
    input = parse_input(file)
    print solve_one(input)
    print solve_two(input)
