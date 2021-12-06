from os import path

PREAMBLE_LEN = 25


def sum_exists(numbers, target):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


# Part 1
def part1(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    for offset in range(len(numbers) - PREAMBLE_LEN):
        subset = numbers[offset:PREAMBLE_LEN + offset]
        target = numbers[PREAMBLE_LEN + offset]
        if not sum_exists(subset, target):
            return target


# Part 2
def part2(inpt: str):
    numbers = [int(n) for n in inpt.splitlines()]
    invalid = part1(inpt)
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers) + 1):
            if sum(numbers[i:j]) == invalid:
                return min(numbers[i:j]) + max(numbers[i:j])


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
