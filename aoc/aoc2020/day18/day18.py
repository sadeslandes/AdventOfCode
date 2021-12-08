from os import path

OPERATIONS = {
    "+": lambda l, r: l + r,
    "*": lambda l, r: l * r
}


def parse(expr):
    return evaluate(*tokenize(expr))


def tokenize(expr):
    group_count = 0
    for idx, c in reversed(list(enumerate(expr))):
        if c == ")":
            group_count += 1
        elif c == "(":
            group_count -= 1
        elif c in OPERATIONS and group_count == 0:
            return (expr[:idx], expr[idx + 1:], OPERATIONS[c])
    # is literal or grouped expression
    return (expr, None, None)


def evaluate(term1, term2, op):
    def is_grouped(expr):
        if expr[0] == "(" and expr[-1] == ")":
            group_count = 0
            for c in expr[1:-1]:
                if c == "(":
                    group_count += 1
                elif c == ")":
                    group_count -= 1
                if group_count < 0:
                    return False
            return True
        return False

    # monomial case (literal or grouped)
    if term2 is None:
        if is_grouped(term1):
            # remove surrounding parentheses
            return parse(term1[1:-1])
        else:
            # is literal
            return int(term1)

    # binomial case
    return op(parse(term1), parse(term2))


def preprocess(expr):
    preprocessed = expr[:]
    if expr.find("*") != -1:
        start = 0
        while (idx := preprocessed.find("+", start)) != -1:
            # find left term
            left_idx = 0
            group_count = 0
            for li in range(idx - 1, -1, -1):
                c = preprocessed[li]
                if c == ")":
                    group_count += 1
                elif c == "(":
                    group_count -= 1
                elif group_count < 0 or (group_count == 0 and c in OPERATIONS):
                    left_idx = li + 1
                    break
            # find right term
            right_idx = len(preprocessed)
            group_count = 0
            for ri in range(idx + 1, len(preprocessed)):
                c = preprocessed[ri]
                if c == "(":
                    group_count += 1
                elif c == ")":
                    group_count -= 1
                elif group_count < 0 or (group_count == 0 and c in OPERATIONS):
                    right_idx = ri
                    break
            preprocessed = (
                preprocessed[:left_idx]
                + "("
                + preprocessed[left_idx:right_idx]
                + ")"
                + preprocessed[right_idx:]
            )
            start = idx + 2
    return preprocessed


# Part 1
def part1(inpt: str):
    inpt_lines = inpt = [line.replace(" ", "") for line in inpt.splitlines()]
    return sum(parse(line) for line in inpt_lines)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt = [line.replace(" ", "") for line in inpt.splitlines()]
    return sum(parse(preprocess(line)) for line in inpt_lines)


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