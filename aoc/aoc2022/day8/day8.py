"""https://adventofcode.com/2022/day/8"""
from __future__ import annotations

from dataclasses import dataclass
from os import path
from typing import Iterator, Tuple


@dataclass(frozen=True)
class Tree:
    position: Tuple[int, int]
    height: int


def make_grid(inpt: str) -> Tuple[Tuple[Tree]]:
    return tuple(
        tuple(Tree((x, y), int(height)) for x, height in enumerate(line))
        for y, line in enumerate(inpt.splitlines())
    )


def generate_lines_of_sight(grid: Tuple[Tuple[Tree]]) -> Iterator[Tuple[Tree]]:
    yield from iter(grid)  # viewed from left
    yield from iter(tuple(reversed(r)) for r in grid)  # viewed from right
    yield from iter(zip(*grid))  # viewed from top
    yield from iter(zip(*reversed(grid)))  # viewed from bottom


# Part 1
def part1(inpt: str):
    grid = make_grid(inpt)
    seen = set()
    for los in generate_lines_of_sight(grid):
        max_height = -1
        for tree in los:
            if tree.height > max_height:
                max_height = tree.height
                seen.add(tree)
    return len(seen)


# Part 2
def part2(inpt: str):
    grid = make_grid(inpt)
    max_score = -1
    num_rows = len(grid)
    num_cols = len(grid[0])
    for y in range(num_rows):
        for x in range(num_cols):
            tree_height = grid[y][x].height
            up, down, left, right = 0, 0, 0, 0
            # look up
            for dy in range(y - 1, -1, -1):
                up += 1
                if grid[dy][x].height >= tree_height:
                    break
            # look down
            for dy in range(y + 1, num_rows):
                down += 1
                if grid[dy][x].height >= tree_height:
                    break
            # look left
            for dx in range(x - 1, -1, -1):
                left += 1
                if grid[y][dx].height >= tree_height:
                    break
            # look right
            for dx in range(x + 1, num_cols):
                right += 1
                if grid[y][dx].height >= tree_height:
                    break

            if (score := up * down * left * right) > max_score:
                max_score = score
    return max_score


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
