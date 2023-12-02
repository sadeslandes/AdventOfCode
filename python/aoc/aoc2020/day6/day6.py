from functools import reduce
from os import path


def parse_input(inpt):
    return [group.split("\n") for group in inpt.split("\n\n")]


# Part 1
def part1(inpt: str):
    responses = parse_input(inpt.rstrip())
    return sum(len(set("".join(g))) for g in responses)


# Part 2
def part2(inpt: str):
    responses = parse_input(inpt.rstrip())

    def group_common_responses(group):
        return reduce(lambda acc, p: set(acc) & set(p), group)

    return sum(len(set(group_common_responses(g))) for g in responses)


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
