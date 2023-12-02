from collections import Counter
from functools import reduce
from os import path

import regex as re


def parse_input(inpt):
    p = re.compile(r"^(e|se|sw|w|nw|ne)+$")
    paths = []
    for line in inpt:
        paths.append(p.match(line).captures(1))
    return paths


def flip_tiles(black_tiles):
    def get_adjacent(tile):
        adjacent = set()
        offsets = [(1, 0), (1, -1), (0, -1), (0, 1), (-1, 0), (-1, 1)]
        for offset in offsets:
            adjacent.add(tuple(sum(z) for z in zip(tile, offset)))
        return adjacent

    new_black_tiles = set()
    all_adjacent = reduce(
        lambda acc, cur: acc.union(get_adjacent(cur)), black_tiles, set()
    )
    for tile in all_adjacent:
        black_adjacent = black_tiles.intersection(get_adjacent(tile))
        if tile in black_tiles and len(black_adjacent) in (1, 2):
            new_black_tiles.add(tile)
        elif tile not in black_tiles and len(black_adjacent) == 2:
            new_black_tiles.add(tile)
    return new_black_tiles


def get_black_tiles(paths):
    def reduce_path(path):
        # From a path return coordinates to a tile in the form (rd, ld)
        # where rd represents travelling along the ne-sw axis (ne+)
        # and ld the nw-se axis (nw+)
        direction_counter = Counter(path)
        rd = (direction_counter["ne"] + direction_counter["e"]) - (
            direction_counter["sw"] + direction_counter["w"]
        )
        ld = (direction_counter["nw"] + direction_counter["w"]) - (
            direction_counter["se"] + direction_counter["e"]
        )
        return (rd, ld)

    path_counts = Counter(reduce_path(p) for p in paths)
    return set(p for p in path_counts if path_counts[p] % 2 == 1)


# Part 1
def part1(inpt: str):
    paths = parse_input(inpt.splitlines())
    black_tiles = get_black_tiles(paths)
    return len(black_tiles)


# Part 2
def part2(inpt: str):
    paths = parse_input(inpt.splitlines())
    black_tiles = get_black_tiles(paths)
    for _ in range(100):
        black_tiles = flip_tiles(black_tiles)
    return len(black_tiles)


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
