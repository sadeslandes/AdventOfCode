"""https://adventofcode.com/2021/day/7"""
from os import path
from functools import cache


@cache
def get_exponential_fuel_cost(n):
    return get_exponential_fuel_cost(n - 1) + n if n else 0


# Part 1
def part1(inpt: str):
    nums = [int(n) for n in inpt.rstrip().split(",")]
    low, high = min(nums), max(nums)
    return sorted(sum(abs(m - n) for n in nums) for m in range(low, high))[0]


# Part 2
def part2(inpt: str):
    nums = sorted(
        int(n) for n in inpt.rstrip().split(",")
    )  # sort to make better use of memoization
    low, high = min(nums), max(nums)
    return sorted(
        sum(get_exponential_fuel_cost(abs(m - n)) for n in nums)
        for m in range(low, high)
    )[0]


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
