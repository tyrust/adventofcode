#!/usr/bin/python
'''
Advent of Code 2015
Day 7

By Tyrus Tenneson
2015-12-15
'''
import os
import re
import sys

# Regexes because I don't want to write a parser.
ASSIGNMENT_REGEX = re.compile(r'(?P<in>[^ ]+) -> (?P<out>.*)')
NOT_REGEX = re.compile(r'NOT (?P<in>[^ ]+) -> (?P<out>.*)')
BINARY_REGEX = re.compile(r'(?P<in1>[^ ]+) (?P<op>[^ ]+) (?P<in2>[^ ]+) -> '
                          r'(?P<out>.*)')

NOT = 'NOT'
AND = 'AND'
OR = 'OR'
LSHIFT = 'LSHIFT'
RSHIFT = 'RSHIFT'

MASK = 0xFFFF

class Circuit:
    def __init__(self, circuit):
        # Make a copy of the dict, lol.
        self._circuit = dict(circuit)

    def eval(self, symbol):
        if symbol not in self._circuit:
            return int(symbol)

        # It's an int, wire, or expression.
        expression = self._circuit[symbol]
        if isinstance(expression, int):
            return expression

        value = None
        if isinstance(expression, str):
            # It is a wire.
            value = self.eval(expression)
        else:
            # Evaluate the expression.
            op = expression[0]
            eval1 = self.eval(expression[1])
            if len(expression) == 3:
                eval2 = self.eval(expression[2])
            # Switch on op.
            if op == NOT:
                value = ~eval1
            elif op == AND:
                value = eval1 & eval2
            elif op == OR:
                value = eval1 | eval2
            elif op == LSHIFT:
                value = eval1 << eval2
            elif op == RSHIFT:
                value = eval1 >> eval2

        # Python numbers are two's compliment.  Our circuit is
        # unsigned.  So we have to mask every number after doing a
        # bitwise operation to convert to unsigned.
        # Idk if this is strictly necessary but it doesn't hurt so
        # w/e.
        value = value & MASK
        self._circuit[symbol] = value
        return value

    def override(self, symbol, value):
        self._circuit[symbol] = value

    def __str__(self):
        return str(self._circuit)


def solve_one(problem):
    circuit = Circuit(problem)
    return circuit.eval('a')


def solve_two(problem):
    circuit = Circuit(problem)
    a_val = circuit.eval('a')
    # Reset circuit
    circuit = Circuit(problem)
    circuit.override('b', a_val)
    return circuit.eval('a')


def parse_problem(f):
    problem = {}
    for l in f.readlines():
        m = ASSIGNMENT_REGEX.match(l)
        if m:
            problem[m.group('out')] = m.group('in')
            continue

        m = NOT_REGEX.match(l)
        if m:
            problem[m.group('out')] = (NOT, m.group('in'))
            continue

        m = BINARY_REGEX.match(l)
        if m:
            problem[m.group('out')] = (m.group('op'),
                                       m.group('in1'), m.group('in2'))
            continue

        # Shouldn't get here
        assert False

    return problem


def print_solutions():
    f = open(os.path.join(sys.path[0], 'input'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
