from dataclasses import dataclass
from os import path


class InfiniteLoopException(Exception):
    pass


@dataclass
class ProgramData:
    accumulator = 0


def run_program(instructions, data):
    index = 0
    visited = set()
    while True:
        if index in visited:
            raise InfiniteLoopException()
        visited.add(index)

        if index == len(instructions):
            return

        op, arg = instructions[index].split(" ")

        if op == "acc":
            data.accumulator += int(arg)
            index += 1
            continue
        if op == "jmp":
            index += int(arg)
            continue
        if op == "nop":
            index += 1
            continue


def generate_instructions_permutations(instructions_list):
    def _replace_each(string, sub, repl):
        seen = set()
        found = -3
        while found != -1:
            found = string.find(sub, found + 3)
            if found not in seen:
                seen.add(found)
                new_string = string[:found] + string[found:].replace(sub, repl, 1)
                yield new_string.split("|")

    yield instructions_list
    instructions_str = "|".join(instructions_list)
    yield from _replace_each(instructions_str, "nop", "jmp")
    yield from _replace_each(instructions_str, "jmp", "nop")


# Part 1
def part1(inpt: str):
    instructions = inpt.splitlines()
    try:
        data = ProgramData()
        run_program(instructions, data)
        return data.accumulator
    except InfiniteLoopException:
        return data.accumulator


# Part 2
def part2(inpt: str):
    instructions = inpt.splitlines()
    for instruction_set in generate_instructions_permutations(instructions):
        try:
            data = ProgramData()
            run_program(instruction_set, data)
            return data.accumulator
        except InfiniteLoopException:
            continue


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
