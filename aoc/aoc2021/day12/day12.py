"""https://adventofcode.com/2021/day/12"""
from os import path
from collections import defaultdict


def get_paths(graph, start, end, repeats=[]):
    paths = set()

    def _helper(current: str, path: list, repeat=None, repeated=False):
        path.append(current)
        if current == end:
            # target reached
            paths.add(",".join(path))
            return
        visited = set(n for n in path if n.islower())
        for next in graph[current]:
            if next not in visited:
                _helper(next, path, repeat, repeated)
                path.pop()
            elif next == repeat and not repeated:
                _helper(next, path, repeat, True)
                path.pop()

    _helper(start, list())
    for repeat in repeats:
        _helper(start, list(), repeat)
    return paths


def make_graph(lines):
    """returns adjacency list representation of graph"""
    adj_list = defaultdict(set)
    for line in lines:
        v1, v2 = line.split('-')
        adj_list[v1].add(v2)
        adj_list[v2].add(v1)
    return adj_list


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    graph = make_graph(inpt_lines)
    paths = get_paths(graph, 'start', 'end')
    return len(paths)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    graph = make_graph(inpt_lines)
    small_caves = [n for n in graph if n.islower() and n != 'start' and n != 'end']
    paths = get_paths(graph, 'start', 'end', small_caves)
    return len(paths)


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
