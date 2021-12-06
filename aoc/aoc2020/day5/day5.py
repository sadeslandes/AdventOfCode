from math import ceil, floor
from os import path


def decode(s):
    def _decode(encoded):
        rng = [0, 2 ** len(encoded) - 1]
        for c in encoded:
            if c == "F" or c == "L":
                rng[1] = floor(sum(rng) / 2)
            elif c == "B" or c == "R":
                rng[0] = ceil(sum(rng) / 2)
            else:
                raise ValueError("One of 'F'/'L' or 'B'/'R' expected")
        return rng[0]

    return (_decode(s[:7]), _decode(s[7:]))


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    result = 0
    for line in inpt_lines:
        row, col = decode(line)
        _id = row * 8 + col
        if _id > result:
            result = _id
    return result


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    ids = set()
    all_ids = set(r * 8 + c for c in range(8) for r in range(128))
    for line in inpt_lines:
        row, col = decode(line)
        ids.add(row * 8 + col)

    missing = sorted(list(all_ids - ids))
    for idx, _id in enumerate(missing):
        if idx == 0:
            continue
        if missing[idx - 1] != _id - 1:
            return _id


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
