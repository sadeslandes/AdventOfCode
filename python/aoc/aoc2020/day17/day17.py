from functools import reduce
from itertools import product
from os import path

ACTIVE = "#"


def initialize(inpt, num_dimemsion):
    _active = set()
    for y in range(len(inpt)):
        for x in range(len(inpt[y])):
            if inpt[y][x] == ACTIVE:
                point = (x, y) + (0,) * (num_dimemsion - 2)
                _active.add(point)
    return _active


def get_neightbors(p, num_dimemsion):
    neighbors = set()
    origin = (0,) * num_dimemsion
    for offset in product([-1, 0, 1], repeat=num_dimemsion):
        if offset != origin:
            neighbors.add(tuple(sum(z) for z in zip(p, offset)))
    return neighbors


def run_cycle(active, num_dimemsion):
    new_active = set()
    all_neighbors = reduce(
        lambda acc, cur: acc | get_neightbors(cur, num_dimemsion), active, set()
    )
    for p in all_neighbors:
        active_neighbors = active & get_neightbors(p, num_dimemsion)
        if p in active and len(active_neighbors) in [2, 3]:
            new_active.add(p)
        elif p not in active and len(active_neighbors) == 3:
            new_active.add(p)
    return new_active


# Part 1
def part1(inpt: str):
    TARGET = 6
    NUM_DIMENSION = 3
    active = initialize(inpt.splitlines(), NUM_DIMENSION)
    for i in range(TARGET):
        active = run_cycle(active, NUM_DIMENSION)
    return len(active)


# Part 2
def part2(inpt: str):
    TARGET = 6
    NUM_DIMENSION = 4
    active = initialize(inpt.splitlines(), NUM_DIMENSION)
    for i in range(TARGET):
        active = run_cycle(active, NUM_DIMENSION)
    return len(active)


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
