"""https://adventofcode.com/2022/day/15"""
import re
from functools import lru_cache
from os import path

from aoc.utils import Timer

TARGET_ROW = 2000000
SEARCH_SPACE = 4000000


def parse_input(inpt: str):
    pattern = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    sensors = dict()
    for line in inpt.splitlines():
        match = pattern.match(line)
        sensor = tuple(map(int, match.group(1, 2)))
        beacon = tuple(map(int, match.group(3, 4)))
        sensors[sensor] = beacon
    return sensors


@lru_cache
def get_distance(p1, p2) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Part 1
def part1(inpt: str):
    sensors = parse_input(inpt)
    impossible = set()
    for sensor, beacon in sensors.items():
        distance = get_distance(sensor, beacon)
        if (diff := abs(TARGET_ROW - sensor[1])) <= distance:
            impossible.add(sensor[0])
            for offset in range(1, distance - diff + 1):
                impossible.add(sensor[0] + offset)
                impossible.add(sensor[0] - offset)
        if beacon[1] == TARGET_ROW:
            impossible.remove(beacon[0])
    return len(impossible)


# Part 2
def part2(inpt: str):
    sensors = parse_input(inpt)
    for sensor, beacon in sensors.items():
        distance = get_distance(sensor, beacon)


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
