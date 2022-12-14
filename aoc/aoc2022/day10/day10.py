"""https://adventofcode.com/2022/day/10"""
from os import path

from advent_of_code_ocr import convert_6


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    X = 1
    changes = [1]
    cycle = 1
    signals = []
    breakpoints = iter([20, 60, 100, 140, 180, 220])
    breakpoint = next(breakpoints)
    for line in inpt_lines:
        if cycle >= breakpoint:
            if cycle == breakpoint:
                signals.append(breakpoint * changes[-1])
            else:
                signals.append(breakpoint * changes[-2])
            try:
                breakpoint = next(breakpoints)
            except StopIteration:
                return sum(signals)
        inst = line.split()
        if inst[0] == "noop":
            cycle += 1
        elif inst[0] == "addx":
            cycle += 2
            X += int(inst[1])
            changes.append(X)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    CRT = []
    X = 1
    cycle = 1
    for line in inpt_lines:
        inst = line.split()
        if inst[0] == "noop":
            if X - 1 <= (cycle % 40) - 1 <= X + 1:
                CRT.append("#")
            else:
                CRT.append(".")
            cycle += 1
        elif inst[0] == "addx":
            if X - 1 <= (cycle % 40) - 1 <= X + 1:
                CRT.append("#")
            else:
                CRT.append(".")
            if X - 1 <= (cycle % 40) <= X + 1:
                CRT.append("#")
            else:
                CRT.append(".")
            cycle += 2
            X += int(inst[1])
    display = "\n".join("".join(CRT[i : i + 40]) for i in range(0, len(CRT), 40))
    return convert_6(display)


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
