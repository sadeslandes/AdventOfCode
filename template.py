"""url_template"""
from os import path


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    pass


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    pass


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
