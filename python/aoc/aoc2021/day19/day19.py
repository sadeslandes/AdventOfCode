"""https://adventofcode.com/2021/day/19"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from itertools import combinations
from operator import attrgetter
from os import path
from typing import List, Set, Tuple


@dataclass(frozen=True)
class Beacon:
    a: int
    b: int
    c: int
    scanner: int

    def __sub__(self, other):
        return BeaconDistance(self, other)


@dataclass(frozen=True)
class BeaconDistance:
    p1: Beacon
    p2: Beacon
    d_a: int = field(init=False)
    d_b: int = field(init=False)
    d_c: int = field(init=False)
    key: tuple = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "d_a", self.p2.a - self.p1.a)
        object.__setattr__(self, "d_b", self.p2.b - self.p1.b)
        object.__setattr__(self, "d_c", self.p2.c - self.p1.c)
        object.__setattr__(
            self, "key", tuple(sorted((abs(self.d_a), abs(self.d_b), abs(self.d_c))))
        )

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other: BeaconDistance) -> bool:
        return self.key == other.key


def parse_input(inpt: str) -> List[Tuple[Beacon]]:
    return [
        tuple(
            Beacon(*(int(x) for x in beacon.split(",")), i)
            for beacon in scanner.splitlines()[1:]
        )
        for i, scanner in enumerate(inpt.split("\n\n"))
    ]


@lru_cache
def calculate_distances(scanner: Tuple[Beacon]) -> Set[BeaconDistance]:
    """Caclculates distances between each pair of beacons in scanner"""
    return set(b2 - b1 for b1, b2 in combinations(scanner, 2))


def make_graph(scanners):
    adjacency_list = defaultdict(list)
    for i in range(len(scanners) - 1):
        for j in range(i + 1, len(scanners)):
            da = calculate_distances(scanners[i])
            db = calculate_distances(scanners[j])
            da_overlap = da & db
            if len(da_overlap) >= 66:  # 66 is 12 choose 2
                da_overlap = sorted(da_overlap, key=attrgetter("key"))
                db_overlap = sorted(db & da, key=attrgetter("key"))
                overlapping_distances1 = list(
                    zip(
                        db_overlap,
                        da_overlap,
                    )
                )
                overlapping_distances2 = list(
                    zip(
                        da_overlap,
                        db_overlap,
                    )
                )
                adjacency_list[i].append((j, overlapping_distances1))
                adjacency_list[j].append((i, overlapping_distances2))
    return adjacency_list


# Part 1
def part1(inpt: str):
    scanners = parse_input(inpt)
    graph = make_graph(scanners)
    seen_beacons = set()
    # traverse graph DFS starting from scanner 0
    # orient all traversed scanners/beacons relative to scanner 0 as you go
    # add each oriented beacon to a set
    return len(seen_beacons)


# Part 2
def part2(inpt: str):
    scanners = parse_input(inpt)
    pass


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
