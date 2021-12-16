"""https://adventofcode.com/2021/day/9"""
from dataclasses import dataclass
from math import prod
from os import path
from typing import List, Tuple

_offsets = [(0, -1), (0, 1), (1, 0), (-1, 0)]


@dataclass(frozen=True)
class DepthMapPoint:
    x: int
    y: int
    depth: int


DepthMapGraph = dict[DepthMapPoint, list[DepthMapPoint]]


def build_flow_graph(lines: List[str]) -> Tuple[DepthMapGraph, List[DepthMapPoint]]:
    """Models the depth map as a series of trees with low points at the root"""
    adj_map: DepthMapGraph = (
        dict()
    )  # adjacency list graph representation with sinks mapping to sources
    sinks: List[DepthMapPoint] = []  # roots of the generated trees (low points)

    # iterate though depth map
    for y in range((y_max := len(lines))):
        for x in range((x_max := len(lines[y]))):
            if (depth := int(lines[y][x])) == 9:
                continue
            # get lowest of adjacent points
            point = DepthMapPoint(x, y, depth)
            low = None
            d2 = depth
            for dx, dy in _offsets:
                x2, y2 = x + dx, y + dy
                if (
                    0 <= x2 < x_max
                    and 0 <= y2 < y_max
                    and (d := int(lines[y2][x2])) < d2
                ):
                    d2 = d
                    low = (x2, y2, d2)
            if low is not None:
                p2 = DepthMapPoint(*low)
                adj_map.setdefault(p2, list()).append(point)
            else:
                sinks.append(point)

    return adj_map, sinks


def get_basin_size(node: DepthMapPoint, flow_graph: DepthMapGraph) -> int:
    return (
        1 + sum(get_basin_size(c, flow_graph) for c in sources)
        if node in flow_graph and (sources := flow_graph[node])
        else 1
    )


# Part 1
def part1(inpt: str):
    _, sinks = build_flow_graph(inpt.splitlines())
    return sum(sink.depth + 1 for sink in sinks)


# Part 2
def part2(inpt: str):
    flow_graph, sinks = build_flow_graph(inpt.splitlines())
    basin_sizes = sorted([get_basin_size(sink, flow_graph) for sink in sinks])
    return prod(basin_sizes[-3:])


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
