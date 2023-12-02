"""https://adventofcode.com/2022/day/13"""
import json
from functools import cmp_to_key
from itertools import zip_longest
from os import path
from typing import List


def compare_packets(p1: List, p2: List) -> int:
    for left, right in zip_longest(p1, p2):
        if left is None:
            return -1
        elif right is None:
            return 1

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
        elif isinstance(left, list) and isinstance(right, list):
            if (result := compare_packets(left, right)) != 0:
                return result
        else:
            if isinstance(left, int):
                if (result := compare_packets([left], right)) != 0:
                    return result
            else:
                if (result := compare_packets(left, [right])) != 0:
                    return result
    return 0


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    packets = [json.loads(line) for line in inpt_lines if line and not line.isspace()]
    pairs = (packets[i : i + 2] for i in range(0, len(packets), 2))
    ordered = []
    for i, pair in enumerate(pairs):
        if compare_packets(*pair) == -1:
            ordered.append(i + 1)
    return sum(ordered)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    packets = [json.loads(line) for line in inpt_lines if line and not line.isspace()]
    m1 = [[2]]
    m2 = [[6]]
    packets.extend((m1, m2))
    packets.sort(key=cmp_to_key(compare_packets))
    return (packets.index(m1) + 1) * (packets.index(m2) + 1)


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
