"""https://adventofcode.com/2022/day/6"""
from os import path


# Part 1
def part1(inpt: str):
    for pos, chunk in ((i + 4, inpt[i : i + 4]) for i in range(len(inpt) - 3)):
        if len(set(chunk)) == 4:
            return pos


# Part 2
def part2(inpt: str):
    for pos, chunk in ((i + 14, inpt[i : i + 14]) for i in range(len(inpt) - 13)):
        if len(set(chunk)) == 14:
            return pos


if __name__ == "__main__":
    from aoc.utils import Timer

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        data = f.readline()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
