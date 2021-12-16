"""https://adventofcode.com/2021/day/15"""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from os import path
from typing import Iterable


@dataclass(frozen=True, eq=True, order=True)
class Point:
    x: int
    y: int

    _offsets = ((0, -1), (0, 1), (1, 0), (-1, 0))

    def get_adjacent(self, max_x, max_y) -> Iterable[Point]:
        return tuple(
            Point(x, y)
            for dx, dy in Point._offsets
            if max_x > (x := self.x + dx) >= 0 and max_y > (y := self.y + dy) >= 0
        )


Graph = dict[Point, set[Point]]


def make_graph(inpt: str, extend=False) -> tuple[Graph, dict[Point, int], int, int]:
    """Returns adjacency list representation of graph, dictionary of weights, and max dimensions (width, height)"""
    graph = dict()
    weights = dict()
    lines = inpt.splitlines()
    height = len(lines)
    width = len(lines[0])
    if extend:
        lines, height, width = extend_input(lines)
    for y in range(height):
        for x in range(width):
            point = Point(x, y)
            weights[point] = int(lines[y][x])
            graph[point] = set(point.get_adjacent(width, height))
    return graph, weights, width, height


def get_shortest_path(
    graph: Graph, weights: dict[Point, int], start: Point, end: Point
):
    visited = set()
    nodes = [(0, start)]
    costs = {start: 0}
    while nodes:
        cost, current = heappop(nodes)
        if current not in visited:
            visited.add(current)
            if current == end:
                return cost

            for adj in graph[current]:
                if adj in visited:
                    continue
                adj_cost = weights[adj] + cost
                if adj not in costs or adj_cost < costs[adj]:
                    costs[adj] = adj_cost
                    heappush(nodes, (adj_cost, adj))


def extend_input(lines: list[str]) -> tuple[list[list[int]], int, int]:
    new_lines = [
        [
            [
                new if (new := og + dx + dy) < 10 else new % 10 + 1
                for dx in range(5)
                for og in map(int, line)
            ]
            for dy in range(5)
        ]
        for line in lines
    ]
    extended = [row for group in zip(*new_lines) for row in group]
    return extended, len(extended), len(extended[0])


# Part 1
def part1(inpt: str):
    graph, weights, width, height = make_graph(inpt)
    start = Point(0, 0)
    end = Point(width - 1, height - 1)
    cost = get_shortest_path(graph, weights, start, end)
    return cost


# Part 2
def part2(inpt: str):
    graph, weights, width, height = make_graph(inpt, extend=True)
    start = Point(0, 0)
    end = Point(width - 1, height - 1)
    cost = get_shortest_path(graph, weights, start, end)
    return cost


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
