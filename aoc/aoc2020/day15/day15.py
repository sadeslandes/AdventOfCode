from collections import deque
from os import path


def find_nth_spoken_word(inpt, target):
    spoken = dict()
    last_spoken = None
    for i in range(target):
        if i < len(inpt):
            last_spoken = inpt[i]
        elif last_spoken not in spoken or len(spoken[last_spoken]) < 2:
            last_spoken = 0
        else:
            last_spoken = abs(spoken[last_spoken][0] - spoken[last_spoken][1])
        spoken.setdefault(last_spoken, deque(maxlen=2)).append(i)
    return last_spoken


# Part 1
def part1(inpt: str):
    numbers = [int(n) for n in inpt.rstrip().split(",")]
    return find_nth_spoken_word(numbers, 2020)


# Part 2
def part2(inpt: str):
    numbers = [int(n) for n in inpt.rstrip().split(",")]
    return find_nth_spoken_word(numbers, 30000000)


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
