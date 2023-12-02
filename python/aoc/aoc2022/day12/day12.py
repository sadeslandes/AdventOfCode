"""https://adventofcode.com/2022/day/12"""
from collections import defaultdict, deque
from os import path
from string import ascii_lowercase
from typing import Dict, List, Tuple

VALUES = dict(**{k: v for v, k in enumerate(ascii_lowercase)}, **{"S": 0, "E": 25})

AdjList = Dict[Tuple[int, int], List[Tuple[int, int]]]


def make_graph(lines: List[str]) -> Tuple[AdjList, Tuple[int, int], Tuple[int, int]]:
    adj_list = defaultdict(list)
    num_rows = len(lines)
    num_cols = len(lines[0])
    start = None
    goal = None
    for r in range(num_rows):
        for c in range(num_cols):
            if lines[r][c] == "S":
                start = (c, r)
            elif lines[r][c] == "E":
                goal = (c, r)
            for offset in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                dx, dy = offset
                if 0 <= (x := c + dx) < num_cols and 0 <= (y := r + dy) < num_rows:
                    if VALUES[lines[y][x]] - VALUES[lines[r][c]] <= 1:
                        adj_list[(c, r)].append((x, y))
    return adj_list, start, goal


def bfs(
    graph: AdjList,
    root: Tuple[int, int],
    goal: Tuple[int, int],
):
    queue = deque([root])
    seen = set([root])
    parents = dict()

    while queue:
        node = queue.popleft()
        if node == goal:
            child = goal
            path = [goal]
            while parent := parents.get(child, None):
                path.append(parent)
                child = parent
            return list(reversed(path))
        for connected in graph[node]:
            if connected not in seen:
                seen.add(connected)
                parents[connected] = node
                queue.append(connected)
    return []


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    graph, start, end = make_graph(inpt_lines)
    path = bfs(graph, start, end)
    return len(path) - 1


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    graph, _, end = make_graph(inpt_lines)
    path = None
    for start in (
        (x, y)
        for x in range(len(inpt_lines[0]))
        for y in range(len(inpt_lines))
        if VALUES[inpt_lines[y][x]] == 0
    ):
        tmppath = bfs(graph, start, end)
        if not path or (tmppath and len(tmppath) < len(path)):
            path = tmppath
    return len(path) - 1


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
