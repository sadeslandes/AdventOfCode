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
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
