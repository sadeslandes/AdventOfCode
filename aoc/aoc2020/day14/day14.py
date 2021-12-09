import re
from os import path


def parse_mask(string):
    m = re.match(r"mask = (?P<mask>[10X]+)", string)
    return m["mask"]


def parse_write(string):
    m = re.match(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)", string)
    return (int(m["addr"]), int(m["val"]))


def apply_mask_to_value(mask, val):
    return (int(mask.replace("X", "1"), 2) & val) | int(mask.replace("X", "0"), 2)


def apply_mask_to_addr(mask, addr):
    addr = f"{addr:036b}"
    for i, c in enumerate(mask):
        if c == "1" or c == "X":
            addr = addr[:i] + c + addr[i + 1:]

    def _generate_permutations(string):
        if string.count("X") == 0:
            yield int(string, 2)
        else:
            yield from _generate_permutations(string.replace("X", "0", 1))
            yield from _generate_permutations(string.replace("X", "1", 1))

    return _generate_permutations(addr)


# Part 1
def part1(inpt: str):
    memory = dict()
    mask = ""
    addr = 0
    val = 0
    for line in inpt.splitlines():
        if line.startswith("mask"):
            mask = parse_mask(line)
        else:
            addr, val = parse_write(line)
            memory[addr] = apply_mask_to_value(mask, val)
    return sum(memory.values())


# Part 2
def part2(inpt: str):
    memory = dict()
    mask = ""
    addr = 0
    val = 0
    for line in inpt.splitlines():
        if line.startswith("mask"):
            mask = parse_mask(line)
        else:
            addr, val = parse_write(line)
            for a in apply_mask_to_addr(mask, addr):
                memory[a] = val
    return sum(memory.values())


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
