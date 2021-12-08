"""https://adventofcode.com/2021/day/6"""
from os import path
from collections import Counter
from functools import cache

_initial_spawn_delay = 8
_spawn_period = 7


def num_fish_spawned(curr_day, days_until_spawn, max_day):
    @cache
    def _num_fish_spawned(start_day, end_day):
        counter = 0
        for n in range(start_day + 1, max_day + 1, _spawn_period):
            counter += 1 + _num_fish_spawned(n + _initial_spawn_delay, end_day)
        return counter
    return _num_fish_spawned(curr_day + days_until_spawn, max_day)


# Part 1
def part1(inpt: str):
    fish = Counter([int(n) for n in inpt.split(",")])
    return sum((num_fish_spawned(0, k, 80) * v) + v for k, v in fish.items())


# Part 2
def part2(inpt: str):
    fish = Counter([int(n) for n in inpt.split(",")])
    return sum((num_fish_spawned(0, k, 256) * v) + v for k, v in fish.items())


if __name__ == "__main__":
    from aoc.utils import Timer
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
