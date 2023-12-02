"""https://adventofcode.com/2022/day/3"""
import string
from functools import reduce
from operator import iand
from os import path

PRIORITY = {c: i + 1 for i, c in enumerate(string.ascii_letters)}


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    total = 0
    for line in inpt_lines:
        mid = len(line) // 2
        common_item_type = next(iter(set(line[:mid]) & set(line[mid:])))
        total += PRIORITY[common_item_type]
    return total


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    total = 0
    for group in [inpt_lines[i : i + 3] for i in range(0, len(inpt_lines), 3)]:
        common_item_type = next(iter(reduce(iand, [set(g) for g in group])))
        total += PRIORITY[common_item_type]
    return total


if __name__ == "__main__":
    from aoc.utils import Timer

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        data = f.read()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
