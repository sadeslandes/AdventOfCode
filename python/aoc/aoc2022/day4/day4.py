"""https://adventofcode.com/2022/day/4"""
from os import path


# Part 1
def part1(inpt: str):
    overlap_count = 0
    inpt_lines = inpt.splitlines()
    for line in inpt_lines:
        a1, a2, b1, b2 = [
            int(x) for assignemnt in line.split(",") for x in assignemnt.split("-")
        ]
        if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
            overlap_count += 1
    return overlap_count


# Part 2
def part2(inpt: str):
    overlap_count = 0
    inpt_lines = inpt.splitlines()
    for line in inpt_lines:
        a1, a2, b1, b2 = [
            int(x) for assignemnt in line.split(",") for x in assignemnt.split("-")
        ]
        if (a2 >= b1 and b2 >= a2) or (b2 >= a1 and a2 >= b2):
            overlap_count += 1
    return overlap_count


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
