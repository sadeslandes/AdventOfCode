from os import path


def parse_commands(commands):
    for command in commands:
        direction, magnitude = command.split(" ")
        yield (direction, int(magnitude))


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    x_pos = 0
    depth = 0
    for direction, magnitude in parse_commands(inpt_lines):
        if direction == "forward":
            x_pos += magnitude
        elif direction == "down":
            depth += magnitude
        elif direction == "up":
            depth -= magnitude
    return x_pos * depth


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    x_pos = 0
    depth = 0
    aim = 0
    for direction, magnitude in parse_commands(inpt_lines):
        if direction == "forward":
            x_pos += magnitude
            depth += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude
    return x_pos * depth


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
