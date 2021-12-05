"""https://adventofcode.com/2021/day/5"""
from os import path
from dataclasses import dataclass
from typing import List, Tuple
from collections import Counter


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse_line_segments(lines_raw: List[str]) -> List[Tuple[Point, Point]]:
    line_segments = []
    for line_raw in lines_raw:
        p1_raw, p2_raw = line_raw.split(" -> ")
        p1 = Point(*map(int, p1_raw.split(",")))
        p2 = Point(*map(int, p2_raw.split(",")))
        line_segments.append((p1, p2))
    return line_segments


def generate_points(lines: List[Tuple[Point, Point]]) -> Tuple[List[Point], List[Point], List[Point]]:
    """returns 3-tuple of list of generated points for vertical, horizontal, diagonal lines"""
    diagonal_lines = list(filter(lambda l: abs(l[0].x - l[1].x) == abs(l[0].y - l[1].y), lines))
    vertical_lines = list(filter(lambda l: l[0].x == l[1].x, lines))
    horizontal_lines = list(filter(lambda l: l[0].y == l[1].y, lines))
    vertical_points = []
    horizontal_points = []
    diagonal_points = []
    for line in vertical_lines:
        p1, p2 = line
        if p1.y < p2.y:
            start, end = p1, p2
        else:
            start, end = p2, p1
        vertical_points.extend(Point(start.x, start.y + o) for o in range(end.y - start.y + 1))
    for line in horizontal_lines:
        p1, p2 = line
        if p1.x < p2.x:
            start, end = p1, p2
        else:
            start, end = p2, p1
        horizontal_points.extend(Point(start.x + o, start.y) for o in range(end.x - start.x + 1))
    for line in diagonal_lines:
        p1, p2 = line
        if p1.x < p2.x:
            start, end = p1, p2
        else:
            start, end = p2, p1
        slope = (p1.y - p2.y)/(p1.x - p2.x)
        if slope == 1:
            diagonal_points.extend(Point(start.x + o, start.y + o) for o in range(end.x - start.x + 1))
        else:
            diagonal_points.extend(Point(start.x + o, start.y - o) for o in range(end.x - start.x + 1))
    return vertical_points, horizontal_points, diagonal_points


# Part 1
def part1(inpt: str):
    lines = parse_line_segments(inpt.splitlines())
    vertical, horizontal, _ = generate_points(lines)
    vent_locations = Counter(vertical + horizontal)
    return len([p for p in vent_locations if vent_locations[p] > 1])


# Part 2
def part2(inpt: str):
    lines = parse_line_segments(inpt.splitlines())
    vertical, horizontal, diagonal = generate_points(lines)
    vent_locations = Counter(vertical + horizontal + diagonal)
    return len([p for p in vent_locations if vent_locations[p] > 1])


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
