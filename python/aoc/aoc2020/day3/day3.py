from os import path


def traverse_map(dy, dx, map):
    x, y = dx, dy
    path = []
    while y < len(map):
        loc = map[y][x % len(map[y])]
        path.append(loc)
        x += dx
        y += dy
    return path


def count_trees(path):
    return path.count("#")


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    path = traverse_map(1, 3, inpt_lines)
    return count_trees(path)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    # (dy,dx)
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    result = 1
    for dy, dx in slopes:
        path = traverse_map(dy, dx, inpt_lines)
        num_trees = count_trees(path)
        result *= num_trees
    return result


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
