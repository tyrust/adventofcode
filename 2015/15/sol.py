#!/usr/bin/python
'''
Advent of Code 2015
Day 15

By Tyrus Tenneson
2015-12-20
'''
from collections import defaultdict
import os
import re
import sys


LINE_RE = re.compile(r'(\w+): ([^,]*), ([^,]*), ([^,]*), ([^,]*), (.*)')
ROOM = 100
CALORIES = 500


class Recipe(defaultdict):
    def __init__(self, initial=None):
        defaultdict.__init__(self, int)
        if initial:
            self.update(initial)

    def __hash__(self):
        return hash(tuple(self.items()))

    def score(self, ingredients):
        if not self.items():
            return float('-inf')
        totals = defaultdict(int)
        for ingredient, amount in self.iteritems():
            for prop, value in ingredients[ingredient].iteritems():
                if prop == 'calories':
                    continue
                totals[prop] += amount * value
        return reduce(lambda x, y: x * max(y, 0), totals.values(), 1)

    def calories(self, ingredients):
        return sum([ingredients[name]['calories'] * value
                    for name, value in self.iteritems()])


def solve_brute(current, room, ingredients):
    if not room:
        return current
    best = Recipe()
    for ingredient, props in ingredients.iteritems():
        new = Recipe(current)
        new[ingredient] += 1
        new.update(solve_brute(new, room - 1, ingredients))
        best = max(best, new, key=lambda recipe: recipe.score(ingredients))
    return best


def solve_one(ingredients):
    # recipe = solve_brute(Recipe(), len(ingredients), ingredients)
    # I'm not sure if this is valid for all inputs, but it works for
    # mine.  The solve_brute line above also works.
    recipe = Recipe({ingredient: 1 for ingredient in ingredients})
    for i in range(sum(recipe.values()), ROOM):
        best = Recipe()
        for ingredient, props in ingredients.iteritems():
            new = Recipe(recipe)
            new[ingredient] += 1
            best = max(best, new, key=lambda recipe: recipe.score(ingredients))
        recipe = best
    print recipe, recipe.score(ingredients)
    return recipe.score(ingredients)


def solve_two(ingredients):
    recipe = Recipe({ingredient: 1 for ingredient in ingredients})
    healthiest = min(ingredients,
                     key=lambda name: ingredients[name]['calories'])
    recipe[healthiest] = ROOM - len(ingredients) + 1
    print recipe, recipe.score(ingredients), recipe.calories(ingredients)
    for i in range(sum(recipe.values()), CALORIES):
        best = Recipe()
        for ingredient, props in ingredients.iteritems():
            new = Recipe(recipe)
            new[ingredient] += 1
            best = max(best, new, key=lambda recipe: recipe.score(ingredients))
        recipe = best
    print recipe, recipe.score(ingredients)
    return recipe.score(ingredients)


def parse_problem(f):
    ingredients = defaultdict(dict)
    for line in f.readlines():
        line = line.strip()
        groups = LINE_RE.match(line).groups()
        ingredient, raw_props = groups[0], groups[1:]
        for raw_prop in raw_props:
            prop, value = raw_prop.split(' ')
            ingredients[ingredient][prop] = int(value)
    return ingredients


def print_solutions():
    f = open(os.path.join(sys.path[0], 'sample'), 'r')
    problem = parse_problem(f)
    print solve_one(problem)
    print solve_two(problem)


if __name__ == '__main__':
    print_solutions()
