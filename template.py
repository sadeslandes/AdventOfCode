"""url_template"""
from os import path


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    pass


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    pass


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
