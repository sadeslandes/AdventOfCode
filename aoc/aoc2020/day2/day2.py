import re
from os import path


def validate_password(password, policy_str, rule):
    regex = re.compile(r"(\d+)-(\d+) (\w+)")
    n1, n2, substr = regex.search(policy_str).groups()
    return rule(int(n1), int(n2), substr, password)


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    valid = 0
    for line in inpt_lines:
        policy, password = line.split(": ")
        if validate_password(
            password, policy, lambda n1, n2, substr, pw: n1 <= pw.count(substr) <= n2
        ):
            valid += 1
    return valid


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    valid = 0
    for line in inpt_lines:
        policy, password = line.split(": ")
        if validate_password(
            password,
            policy,
            lambda n1, n2, substr, pw: (
                (pw[n1 - 1] == substr) ^ (pw[n2 - 1] == substr)
            ),
        ):
            valid += 1
    return valid


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
