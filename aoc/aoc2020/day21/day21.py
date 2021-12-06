from collections import Counter
from os import path

import regex as re


def parse_ingredients(recipes):
    p = re.compile(r"^(?:(\w+) )+\(contains (?:(\w+)(?:, )?)+\)$")
    allergen_map = dict()
    ingredient_counts = Counter()
    for recipe in recipes:
        m = p.match(recipe)
        ingredients = set(m.captures(1))
        allergens = m.captures(2)
        ingredient_counts.update(ingredients)
        for allergen in allergens:
            try:
                allergen_map[allergen] &= ingredients
            except KeyError:
                allergen_map[allergen] = set(ingredients)
    return ingredient_counts, allergen_map


# Part 1
def part1(inpt: str):
    ingredient_counts, allergen_map = parse_ingredients(inpt.splitlines())
    possible_allergens = set().union(*allergen_map.values())
    not_allergens = set(ingredient_counts.keys()) - possible_allergens
    return sum(ingredient_counts[ingredient] for ingredient in not_allergens)


# Part 2
def part2(inpt: str):
    _, allergen_map = parse_ingredients(inpt.splitlines())
    fully_constrained = dict()
    allergen_map = dict(allergen_map)  # make copy
    while len(allergen_map) > 0:
        propagate = None
        for allergen in allergen_map:
            if len(allergen_map[allergen]) == 1:
                encoded_allergen = next(iter(allergen_map[allergen]))
                propagate = allergen_map[allergen]
                fully_constrained[allergen] = encoded_allergen
                del allergen_map[allergen]
                break
        for allergen in allergen_map:
            allergen_map[allergen] -= propagate
    return ",".join((fully_constrained[a] for a in sorted(fully_constrained)))


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
