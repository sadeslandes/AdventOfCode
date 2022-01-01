"""
https://adventofcode.com/2021/day/17
credit to https://github.com/charelF/AdventOfCode/blob/ac1a9b7349c40db9db8cc616609a4032f7f19490/aoc.ipynb for explanations
"""
from dataclasses import dataclass
from os import path
from typing import Iterator


@dataclass
class Point:
    x: int
    y: int


def throw(vx: int, vy: int) -> Iterator[Point]:
    """Generator for points in arc"""
    x, y = 0, 0
    while True:
        x += vx
        y += vy
        vx = vx + 1 if vx < 0 else vx - 1 if vx > 0 else 0
        vy -= 1
        yield Point(x, y)


def evaluate_throw(vx: int, vy: int, target: tuple[Point, Point]) -> int:
    """Determines whether a point in the thrown arc lands in the target area. Returns the max height of the arc"""
    max_height = 0
    top_left, bottom_right = target
    for point in throw(vx, vy):
        max_height = max(max_height, point.y)
        # if we are past the target area then stop
        if point.x > bottom_right.x or point.y < bottom_right.y:
            return None
        # check in in bounds
        if (
            top_left.x <= point.x <= bottom_right.x
            and top_left.y >= point.y >= bottom_right.y
        ):
            return max_height


def parse_target(inpt: str) -> tuple[int, int, int, int]:
    return tuple(
        int(n)
        for s in inpt[len("target area: ") :].split(", ")
        for n in s[2:].split("..")
    )


def last_summand(target):
    n = 0
    for i in range(target):
        n += i
        if n >= target:
            return i


# Part 1
def part1(inpt: str):
    _, _, ymax, _ = parse_target(inpt.rstrip())
    # probe comes down with same y velocity as it was shot up at therefore there will always be
    # some time step at which the probe is at point (x, 0). To find the higest apex we need to maximize
    # y velocity at y=0 such that it still lands in the target. This means y velocity at y=0 === target ymin
    # since y velocity decreases by 1 at each step max height can by found by taking the triangle number of max y velocity
    return sum(range(abs(ymax)))


# Part 2
def part2(inpt: str):
    xmin, xmax, ymax, ymin = parse_target(inpt.rstrip())
    target = (Point(xmin, ymin), Point(xmax, ymax))
    count = 0
    for x in range(
        last_summand(xmin), xmax + 1
    ):  # anything lower never reaches target, higher overshoots on fist step
        for y in range(
            ymax, 1 - ymax
        ):  # anything lower overshoots on first step, higher and target is overshot coming down from apex
            height = evaluate_throw(x, y, target)
            if height is not None:
                count += 1
    return count


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
