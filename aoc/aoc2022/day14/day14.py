"""https://adventofcode.com/2022/day/14"""
from itertools import pairwise
from os import path
from typing import Set, Tuple


def make_point(point_str: str) -> Tuple[int, int]:
    return tuple(map(int, point_str.split(",")))


def place_obstacles(inpt: str) -> Set[Tuple[int, int]]:
    obstacles = set()
    for line in inpt.splitlines():
        points = [make_point(p.strip()) for p in line.split("->")]
        for p1, p2 in pairwise(points):
            if p1[0] == p2[0]:
                # vertical
                if p1[1] < p2[1]:
                    lower, higher = p1[1], p2[1]
                else:
                    lower, higher = p2[1], p1[1]
                for y in range(lower, higher + 1):
                    obstacles.add((p1[0], y))
            else:
                # horizontal
                if p1[0] < p2[0]:
                    left, right = p1[0], p2[0]
                else:
                    left, right = p2[0], p1[0]
                for x in range(left, right + 1):
                    obstacles.add((x, p1[1]))
    return obstacles


# Part 1
def part1(inpt: str):
    obstacles = place_obstacles(inpt)
    leftmost = None
    rightmost = None
    bottommost = None
    for p in obstacles:
        if not leftmost or p[0] < leftmost:
            leftmost = p[0]
        if not rightmost or p[0] > rightmost:
            rightmost = p[0]
        if not bottommost or p[1] > bottommost:
            bottommost = p[1]
    origin = (500, 0)
    settled = 0
    stop_producing = False
    while not stop_producing:
        # produce sand
        x, y = origin
        while True:
            # settle sand
            if x > rightmost or x < leftmost or y > bottommost:
                stop_producing = True
                break

            if (x, y + 1) not in obstacles:
                y += 1
                continue
            if (x - 1, y + 1) not in obstacles:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in obstacles:
                x += 1
                y += 1
                continue

            obstacles.add((x, y))
            settled += 1
            break
    return settled


# Part 2
def part2(inpt: str):
    obstacles = place_obstacles(inpt)
    bottommost = None
    for p in obstacles:
        if not bottommost or p[1] > bottommost:
            bottommost = p[1]
    origin = (500, 0)
    settled = 0
    stop_producing = False
    while not stop_producing:
        # produce sand
        x, y = origin
        while True:
            # settle sand
            if y == bottommost + 1:
                obstacles.add((x, y))
                settled += 1
                break

            if (x, y + 1) not in obstacles:
                y += 1
                continue
            if (x - 1, y + 1) not in obstacles:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in obstacles:
                x += 1
                y += 1
                continue

            if x == 500 and y == 0:
                settled += 1
                stop_producing = True
                break

            obstacles.add((x, y))
            settled += 1
            break
    return settled


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
