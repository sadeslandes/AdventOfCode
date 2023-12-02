"""https://adventofcode.com/2022/day/6"""
from collections import deque
from itertools import islice
from os import path


# Part 1
def part1(inpt: str):
    window_size = 4
    itr = iter(inpt)
    window = deque(islice(itr, window_size - 1), maxlen=window_size)
    pos = window_size - 1
    for c in itr:
        pos += 1
        window.append(c)
        if len(set(window)) == window_size:
            return pos


# Part 2
def part2(inpt: str):
    window_size = 14
    itr = iter(inpt)
    window = deque(islice(itr, window_size - 1), maxlen=window_size)
    pos = window_size - 1
    for c in itr:
        pos += 1
        window.append(c)
        if len(set(window)) == window_size:
            return pos


if __name__ == "__main__":
    from aoc.utils import Timer

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        data = f.readline()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
