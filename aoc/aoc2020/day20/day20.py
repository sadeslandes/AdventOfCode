from functools import reduce
from math import sqrt
from os import path

import regex as re


class Tile:
    @staticmethod
    def from_string(string):
        id_str, *rows = string.splitlines()
        _id = int(re.search(r"Tile (\d+):", id_str)[1])
        return Tile(_id, rows)

    @staticmethod
    def get_permutations(tile):
        perms = set()
        for t in (tile, tile.flip_vertical()):
            for d in range(0, 360, 90):
                perms.add(t.rotate(d))
        return perms

    def __init__(self, _id, rows):
        self.rows = tuple(rows)
        self.id = _id

    def __hash__(self):
        return hash("|".join(self.rows))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return "\n".join(s for s in self.rows)

    def __repr__(self):
        return f"Tile {self.id}"

    def flip_vertical(self):
        return Tile(self.id, list(reversed(self.rows)))

    def flip_horizontal(self):
        return Tile(self.id, [r[::-1] for r in self.rows])

    def rotate(self, degrees=90):
        def transpose(matrix):
            return ["".join(r) for r in zip(*matrix)]

        if degrees == 0:
            return Tile(self.id, self.rows)
        if degrees == 90:
            return Tile(self.id, [r[::-1] for r in transpose(self.rows)])
        if degrees == 180:
            return Tile(self.id, list(reversed([r[::-1] for r in self.rows])))
        if degrees == 270:
            return Tile(self.id, list(reversed([r for r in transpose(self.rows)])))

    def aligns_with(self, edge, other):
        if edge == "top":
            return self.rows[0] == other.rows[-1]
        elif edge == "botton":
            return self.rows[-1] == other.rows[0]
        elif edge == "left":
            this_left = "".join(list(zip(*self.rows))[0])
            other_right = "".join(list(zip(*other.rows))[-1])
            return this_left == other_right
        elif edge == "right":
            this_right = "".join(list(zip(*self.rows))[-1])
            other_left = "".join(list(zip(*other.rows))[0])
            return this_right == other_left


def build_image(grid, tiles, ids, size, row=0, col=0):
    def validate_edges(grid, row, col):
        this = grid[row][col]
        for offset in [(-1, 0, "top"), (0, -1, "left")]:
            r, c = row + offset[0], col + offset[1]
            if r < 0 or c < 0:
                continue
            other = grid[r][c]
            if not this.aligns_with(offset[2], other):
                return False
        return True

    if len(ids) == 0:
        return True
    for _id in ids:
        tile = tiles[_id]
        for perm in Tile.get_permutations(tile):
            grid[row].append(perm)
            if validate_edges(grid, row, col):
                next_col = col + 1 if col + 1 < size else 0
                next_row = row if col + 1 < size else row + 1
                if build_image(
                    grid, tiles, ids - {_id}, size, row=next_row, col=next_col
                ):
                    return True
            grid[row].pop()


def count_monsters(image):
    count = 0
    p_top = re.compile(r"..................#.")
    p_middle = re.compile(r"#....##....##....###")
    p_bottom = re.compile(r".#..#..#..#..#..#...")
    for i in range(2, len(image.rows)):
        for match in p_bottom.finditer(image.rows[i], overlapped=True):
            middle_match = p_middle.match(image.rows[i - 1], match.start(), match.end())
            top_match = p_top.match(image.rows[i - 2], match.start(), match.end())
            if middle_match and top_match:
                count += 1
    return count


# Part 1
def part1(inpt: str):
    grids = inpt.rstrip().split("\n\n")
    grid_len = int(sqrt(len(grids)))
    tiles = {t.id: t for t in (Tile.from_string(tile) for tile in grids)}
    ids = set(tiles.keys())
    grid = [list() for i in range(grid_len)]
    build_image(grid, tiles, ids, grid_len)
    return reduce(
        lambda acc, cur: acc * cur,
        (t.id for r in (grid[0], grid[-1]) for t in (r[0], r[-1])),
        1,
    )


# Part 2
def part2(inpt: str):
    grids = inpt.rstrip().split("\n\n")
    grid_len = int(sqrt(len(grids)))
    tiles = {t.id: t for t in (Tile.from_string(tile) for tile in grids)}
    ids = set(tiles.keys())
    grid = [list() for i in range(grid_len)]
    build_image(grid, tiles, ids, grid_len)
    image_row_size = len(grid[0][0].rows) - 2
    image_rows = [""] * len(grid) * image_row_size
    for grid_row_num, row in enumerate(grid):
        for tile in row:
            for tile_row_num, tile_row in enumerate(tile.rows[1:-1]):
                image_row = grid_row_num * image_row_size + tile_row_num
                image_rows[image_row] += tile_row[1:-1]
    image = Tile(1, image_rows)
    for perm in Tile.get_permutations(image):
        monster_count = count_monsters(perm)
        if monster_count > 0:
            return str(perm).count("#") - (15 * monster_count)


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