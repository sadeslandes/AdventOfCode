from itertools import product
from os import path

OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."


def hash_layout(layout):
    return "".join(layout)


def get_adjacent(layout, row, col):
    adjacent = []
    for offset in product((-1, 0, 1), repeat=2):
        r = row + offset[0]
        c = col + offset[1]
        if r >= 0 and c >= 0 and not (r == row and c == col):
            try:
                adjacent.append(layout[r][c])
            except IndexError:
                pass
    return adjacent


def get_visible(layout, row, col):
    offsets = [
        (0, -1),  # left
        (0, 1),  # right
        (-1, 0),  # up
        (1, 0),  # down
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1),  # down-right
    ]
    visible = []
    for offset in offsets:
        r, c = row, col
        while True:
            r += offset[0]
            c += offset[1]
            if c < 0 or r < 0:
                break
            try:
                if (val := layout[r][c]) != FLOOR:
                    visible.append(val)
                    break
            except IndexError:
                break
    return visible


# Part 1
def part1(inpt: str):
    layout = inpt.splitlines()
    states = set()
    while (hashed := hash_layout(layout)) not in states:
        states.add(hashed)
        new_layout = []
        for r in range(len(layout)):
            new_row = ""
            for c in range(len(layout[r])):
                adj = get_adjacent(layout, r, c)
                if layout[r][c] == EMPTY and adj.count(OCCUPIED) == 0:
                    new_row += OCCUPIED
                elif layout[r][c] == OCCUPIED and adj.count(OCCUPIED) >= 4:
                    new_row += EMPTY
                else:
                    new_row += layout[r][c]
            new_layout.append(new_row)
        layout = new_layout
    return sum(r.count(OCCUPIED) for r in layout)


# Part 2
def part2(inpt: str):
    layout = inpt.splitlines()
    states = set()
    while (hashed := hash_layout(layout)) not in states:
        states.add(hashed)
        new_layout = []
        for r in range(len(layout)):
            new_row = ""
            for c in range(len(layout[r])):
                vis = get_visible(layout, r, c)
                if layout[r][c] == EMPTY and vis.count(OCCUPIED) == 0:
                    new_row += OCCUPIED
                elif layout[r][c] == OCCUPIED and vis.count(OCCUPIED) >= 5:
                    new_row += EMPTY
                else:
                    new_row += layout[r][c]
            new_layout.append(new_row)
        layout = new_layout
    return sum(r.count(OCCUPIED) for r in layout)


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
