"""https://adventofcode.com/2022/day/9"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import pairwise
from os import path


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def is_adjacent(self, other: Point) -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1


def move_knot(direction: str, knot: Point) -> None:
    if direction == "L":
        knot.x -= 1
    elif direction == "R":
        knot.x += 1
    elif direction == "U":
        knot.y -= 1
    elif direction == "D":
        knot.y += 1
    else:
        raise ValueError(f"unexpected direction {direction}")


def follow_knot(leader: Point, follower: Point) -> None:
    if not leader.is_adjacent(follower):
        if leader.y > follower.y:
            # up
            follower.y += 1
        elif leader.y < follower.y:
            # down
            follower.y -= 1

        if leader.x > follower.x:
            # right
            follower.x += 1
        elif leader.x < follower.x:
            # left
            follower.x -= 1


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    head = Point()
    tail = Point()
    visited = set()
    visited.add((tail.x, tail.y))
    for instruction in inpt_lines:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            move_knot(direction, head)
            follow_knot(head, tail)
            visited.add((tail.x, tail.y))
    return len(visited)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    points = [Point() for _ in range(10)]
    head = points[0]
    tail = points[-1]
    visited = set()
    visited.add((tail.x, tail.y))
    for instruction in inpt_lines:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            move_knot(direction, head)
            for p1, p2 in pairwise(points):
                follow_knot(p1, p2)
            visited.add((tail.x, tail.y))
    return len(visited)


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
