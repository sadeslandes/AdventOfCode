from os import path


def count_leaves(numbers):
    appearances = {n: 0 for n in numbers}
    # initialize smallest value with one appearance
    appearances[numbers[0]] = 1
    for idx, n in enumerate(numbers):
        offset_idx = idx - 1
        while offset_idx >= 0 and numbers[offset_idx] >= n - 3:
            appearances[n] += appearances[numbers[offset_idx]]
            offset_idx -= 1
    return appearances[numbers[-1]]


# Part 1
def part1(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    jolts = 0
    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for n in sorted(numbers):
        counts[n - jolts] += 1
        jolts = n
    # for built in adapter
    counts[3] += 1
    return counts[1] * counts[3]


# Part 2
def part2(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    counts = 0
    sorted_numbers = sorted(numbers)
    for idx, n in enumerate(sorted_numbers):
        if n <= 3:
            counts += count_leaves(sorted_numbers[idx:])
        else:
            break
    return counts


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