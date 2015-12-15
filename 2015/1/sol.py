#!/usr/bin/python

def solve_one(input):
    return sum([1 if c == '(' else -1 for c in input])

def solve_two(input):
    floor = 0
    for idx, c in enumerate(input):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return idx + 1

def parse_input(file):
    return file.read().strip()

if __name__ == '__main__':
    file = open('input', 'r')
    input = parse_input(file)
    print solve_one(input)
    print solve_two(input)
