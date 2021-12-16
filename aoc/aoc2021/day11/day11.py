"""https://adventofcode.com/2021/day/11"""
from itertools import product
from os import path
from typing import List


def get_neighbors(p):
    origin = (0, 0)
    for offset in product([-1, 0, 1], repeat=2):
        if offset != origin:
            yield tuple(sum(z) for z in zip(p, offset))


def simulate_step(grid: List[List[int]]) -> int:
    """Simulates a single step of energizing and flashing of octopuses, returning number of flashes"""
    flash = set()
    processed = set()
    # increment energy and update flash
    for key in grid:
        grid[key] += 1
        if grid[key] > 9:
            flash.add(key)
    # process flashes
    while flash:
        tmp = set()
        for o in flash:
            # energize neighbors
            for n in get_neighbors(o):
                try:
                    grid[n] += 1
                except KeyError:
                    continue
                if grid[n] > 9:
                    tmp.add(n)
        # move octopus to processed
        processed |= flash
        flash = tmp - processed
    # reset processed octopus energy
    for o in processed:
        grid[o] = 0
    return len(processed)


# Part 1
def part1(inpt: str):
    grid = {
        (x, y): int(n)
        for y, row in enumerate(inpt.splitlines())
        for x, n in enumerate(row)
    }
    return sum(simulate_step(grid) for _ in range(100))


# Part 2
def part2(inpt: str):
    grid = {
        (x, y): int(n)
        for y, row in enumerate(inpt.splitlines())
        for x, n in enumerate(row)
    }
    steps = 1
    while simulate_step(grid) != 100:
        steps += 1
    return steps


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
