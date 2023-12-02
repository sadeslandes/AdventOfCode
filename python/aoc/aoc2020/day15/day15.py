from os import path


def find_nth_spoken_word(inpt, target):
    spoken = {n: i + 1 for i, n in enumerate(inpt[:-1])}
    last_spoken = inpt[-1]
    for turn in range(len(inpt), target):
        next_spoken = turn - spoken[last_spoken] if last_spoken in spoken else 0
        spoken[last_spoken] = turn
        last_spoken = next_spoken
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
