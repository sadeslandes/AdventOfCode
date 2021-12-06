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
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
