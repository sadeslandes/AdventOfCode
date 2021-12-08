from itertools import combinations
from os import path


# Part 1
def part1(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    for c in combinations(numbers, 2):
        if sum(c) == 2020:
            return c[0] * c[1]


# Part 2
def part2(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    for c in combinations(numbers, 3):
        if sum(c) == 2020:
            return c[0] * c[1] * c[2]


if __name__ == "__main__":
    from aoc.utils import Timer
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
