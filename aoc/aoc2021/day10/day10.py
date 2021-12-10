"""https://adventofcode.com/2021/day/10"""
from os import path

_openings = {"(", "[", "{", "<"}
_closing_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


# Part 1
def part1(inpt: str):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    inpt_lines = inpt.splitlines()
    score = 0
    for line in inpt_lines:
        chunk_stack = []
        for c in line:
            if c in _openings:
                chunk_stack.append(c)
            elif chunk_stack[-1] != _closing_map[c]:
                # corrupted line (illegal closing)
                score += points[c]
                chunk_stack.pop()
                break
            else:
                chunk_stack.pop()
    return score


# Part 2
def part2(inpt: str):
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    inpt_lines = inpt.splitlines()
    scores = []
    for line in inpt_lines:
        score = 0
        chunk_stack = []
        for c in line:
            if c in _openings:
                chunk_stack.append(c)
            elif chunk_stack[-1] != _closing_map[c]:
                # corrupted line (illegal closing)
                chunk_stack.clear()
                break
            else:
                chunk_stack.pop()
        if chunk_stack:
            # line is incomplete
            for opening in reversed(chunk_stack):
                score *= 5
                score += points[opening]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]  # number of incomplete lines is always odd


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
