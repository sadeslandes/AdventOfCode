"""https://adventofcode.com/2021/day/13"""
from dataclasses import dataclass
from enum import Enum, auto
from os import path
from typing import Iterable

from advent_of_code_ocr import convert_6


class FoldAxis(Enum):
    VERTICAL = (auto(),)
    HORIZONTAL = auto()


@dataclass
class Fold:
    axis: FoldAxis
    value: int


@dataclass(frozen=True)
class Dot:
    x: int
    y: int


def parse_input(inpt) -> tuple[set[Dot], list[Fold]]:
    folds = list()
    dots = set()
    points, instructions = inpt.split("\n\n")
    points, instructions = points.splitlines(), instructions.splitlines()
    for point in points:
        coordinates = (int(v) for v in point.split(","))
        dots.add(Dot(*coordinates))
    instruction_start = len("fold along ")
    for instruction in instructions:
        axis, value = instruction[instruction_start:].split("=")
        axis = FoldAxis.HORIZONTAL if axis == "y" else FoldAxis.VERTICAL
        value = int(value)
        folds.append(Fold(axis, value))
    return dots, folds


def do_fold(dots: Iterable[Dot], fold: Fold) -> None:
    new_dots = set()
    if fold.axis == FoldAxis.HORIZONTAL:

        def get_value(d: Dot):
            return d.y

        def factory(d: Dot, new: int):
            return Dot(d.x, new)

    else:

        def get_value(d: Dot):
            return d.x

        def factory(d: Dot, new: int):
            return Dot(new, d.y)

    for dot in dots:
        old_value = get_value(dot)

        if old_value > fold.value:
            new_value = fold.value - abs(fold.value - old_value)
            new_dots.add(factory(dot, new_value))
        else:
            new_dots.add(dot)
    return new_dots


def stringify_dots(dots: Iterable[Dot]) -> str:
    width = max(dot.x for dot in dots) + 1
    height = max(dot.y for dot in dots) + 1
    line = ["."] * width
    lines = [list(line) for _ in range(height)]
    for dot in dots:
        lines[dot.y][dot.x] = "#"
    return "\n".join("".join(line) for line in lines)


# Part 1
def part1(inpt: str):
    dots, folds = parse_input(inpt)
    dots = do_fold(dots, folds[0])
    return len(dots)


# Part 2
def part2(inpt: str):
    dots, folds = parse_input(inpt)
    for fold in folds:
        dots = do_fold(dots, fold)
    return convert_6(stringify_dots(dots))


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
