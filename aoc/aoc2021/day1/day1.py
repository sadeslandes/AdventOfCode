"""https://adventofcode.com/2021/day/1"""
from os import path


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    increase_count = 0
    depths = [int(i) for i in inpt_lines]
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increase_count += 1
    return increase_count


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    prev_sum = None
    increase_count = 0
    depths = [int(i) for i in inpt_lines]
    for i in range(2, len(depths)):
        curr_sum = sum(depths[i - 2: i + 1])
        if prev_sum is not None and curr_sum > prev_sum:
            increase_count += 1
        prev_sum = curr_sum
    return increase_count


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
