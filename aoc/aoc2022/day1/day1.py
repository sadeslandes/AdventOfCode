"""https://adventofcode.com/2022/day/1"""
from os import path


# Part 1
def part1(inpt: str):
    max_total = 0
    total = 0
    for line in inpt.splitlines():
        if line:
            total += int(line)
        else:
            max_total = max(max_total, total)
            total = 0
    max_total = max(max_total, total)
    return max_total


# Part 2
def part2(inpt: str):
    totals = []
    total = 0
    for line in inpt.splitlines():
        if line:
            total += int(line)
        else:
            totals.append(total)
            total = 0
    totals.append(total)
    return sum(sorted(totals)[-3:])


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
