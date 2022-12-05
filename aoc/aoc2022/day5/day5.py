"""https://adventofcode.com/2022/day/5"""
from os import path
from collections import defaultdict
import re


def parse_input(inpt: str):
    crates, instructions = inpt.split("\n\n")
    return parse_stacks(crates), parse_instructions(instructions)


def parse_stacks(crates: str):
    stacks = defaultdict(list)
    idx_map = dict()
    for line in reversed(crates.splitlines()):
        for i, c in enumerate(line):
            if c.isdecimal():
                idx_map[i] = int(c)
            elif c.isalpha():
                stacks[idx_map[i]].append(c)
    return stacks


def parse_instructions(instructions: str):
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    return [
        tuple(int(n) for n in pattern.match(line).groups())
        for line in instructions.splitlines()
    ]


# Part 1
def part1(inpt: str):
    stacks, instructions = parse_input(inpt)
    for count, src, dst in instructions:
        for _ in range(count):
            stacks[dst].append(stacks[src].pop())
    return "".join(stacks[i + 1][-1] for i in range(len(stacks)))


# Part 2
def part2(inpt: str):
    stacks, instructions = parse_input(inpt)
    for count, src, dst in instructions:
        stacks[dst] += stacks[src][-1 * count :]
        del stacks[src][-1 * count :]
    return "".join(stacks[i + 1][-1] for i in range(len(stacks)))


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
