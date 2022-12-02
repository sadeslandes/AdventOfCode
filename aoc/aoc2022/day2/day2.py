"""https://adventofcode.com/2022/day/2"""
from os import path

HAND_SCORES = {
    "R": 1,
    "P": 2,
    "S": 3,
}

OUTCOME_SCORES = {
    "L": 0,
    "D": 3,
    "W": 6,
    "X": 0,
    "Y": 3,
    "Z": 6,
}

HAND_MAP = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

HANDS = ("S", "R", "P")


def judge_hand(opponent, you):
    if opponent == you:
        return "D"
    elif you == HANDS[(HAND_SCORES[opponent] + 1) % 3]:
        return "W"
    else:
        return "L"


def derive_hand(opponent, outcome):
    if outcome == "Y":  # draw
        return opponent
    elif outcome == "X":  # lose
        return HANDS[(HAND_SCORES[opponent] - 1) % 3]
    else:  # win
        return HANDS[(HAND_SCORES[opponent] + 1) % 3]


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    total = 0
    for line in inpt_lines:
        opponent, you = [HAND_MAP[x] for x in line.split()]
        total += OUTCOME_SCORES[judge_hand(opponent, you)] + HAND_SCORES[you]
    return total


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    total = 0
    for line in inpt_lines:
        opponent, outcome = line.split()
        total += (
            OUTCOME_SCORES[outcome]
            + HAND_SCORES[derive_hand(HAND_MAP[opponent], outcome)]
        )
    return total


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
