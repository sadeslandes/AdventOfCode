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
    if outcome == "D":  # draw
        return opponent
    elif outcome == "L":  # lose
        return HANDS[(HAND_SCORES[opponent] - 1) % 3]
    else:  # win
        return HANDS[(HAND_SCORES[opponent] + 1) % 3]


# Part 1
def part1(inpt: str):
    trans_table = str.maketrans("ABCXYZ", "RPSRPS", " ")
    inpt_lines = inpt.translate(trans_table).splitlines()
    total = 0
    for opponent, you in inpt_lines:
        total += OUTCOME_SCORES[judge_hand(opponent, you)] + HAND_SCORES[you]
    return total


# Part 2
def part2(inpt: str):
    trans_table = str.maketrans("ABCXYZ", "RPSLDW", " ")
    inpt_lines = inpt.translate(trans_table).splitlines()
    total = 0
    for opponent, outcome in inpt_lines:
        total += OUTCOME_SCORES[outcome] + HAND_SCORES[derive_hand(opponent, outcome)]
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
