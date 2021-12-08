from collections import namedtuple
from os import path

Position = namedtuple("Position", ["x", "y"])
ShipBearing = namedtuple("ShipBearing", ["direction", "position"])

EAST = "E"
SOUTH = "S"
WEST = "W"
NORTH = "N"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"
DIRECTIONS = [EAST, SOUTH, WEST, NORTH]


def update_bearings(bearing, op, arg):
    if op == EAST:
        new_dx = bearing.position.x + arg
        return ShipBearing(bearing.direction, Position(new_dx, bearing.position.y))
    if op == SOUTH:
        new_dy = bearing.position.y - arg
        return ShipBearing(bearing.direction, Position(bearing.position.x, new_dy))
    if op == WEST:
        new_dx = bearing.position.x - arg
        return ShipBearing(bearing.direction, Position(new_dx, bearing.position.y))
    if op == NORTH:
        new_dy = bearing.position.y + arg
        return ShipBearing(bearing.direction, Position(bearing.position.x, new_dy))
    if op == LEFT:
        direction_idx = DIRECTIONS.index(bearing.direction)
        new_idx = (direction_idx - (arg // 90)) % len(DIRECTIONS)
        new_direction = DIRECTIONS[new_idx]
        return ShipBearing(new_direction, bearing.position)
    if op == RIGHT:
        direction_idx = DIRECTIONS.index(bearing.direction)
        new_idx = (direction_idx + (arg // 90)) % len(DIRECTIONS)
        new_direction = DIRECTIONS[new_idx]
        return ShipBearing(new_direction, bearing.position)
    if op == FORWARD:
        return update_bearings(bearing, bearing.direction, arg)


def update_waypoint(waypoint, op, arg):
    if op == FORWARD:
        # shouldn't happen
        raise ValueError("FORWARD not valid for waypoint")
    if op == EAST:
        new_x = waypoint.x + arg
        return Position(new_x, waypoint.y)
    if op == SOUTH:
        new_y = waypoint.y - arg
        return Position(waypoint.x, new_y)
    if op == WEST:
        new_x = waypoint.x - arg
        return Position(new_x, waypoint.y)
    if op == NORTH:
        new_y = waypoint.y + arg
        return Position(waypoint.x, new_y)
    # rotations
    if waypoint.x == 0 and waypoint.y == 0:
        return waypoint
    if arg == 180:
        return Position(-1 * waypoint.x, -1 * waypoint.y)
    if (op == LEFT and arg == 90) or (op == RIGHT and arg == 270):
        return Position(-1 * waypoint.y, waypoint.x)
    if (op == RIGHT and arg == 90) or (op == LEFT and arg == 270):
        return Position(waypoint.y, -1 * waypoint.x)


def move_ship(ship, waypoint, arg):
    return Position(ship.x + (arg * waypoint.x), ship.y + (arg * waypoint.y))


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    bearing = ShipBearing(EAST, Position(0, 0))
    for line in inpt_lines:
        op, arg = line[0], int(line[1:])
        bearing = update_bearings(bearing, op, arg)
    return abs(bearing.position.x) + abs(bearing.position.y)


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    ship = Position(0, 0)
    waypoint = Position(10, 1)
    for line in inpt_lines:
        op, arg = line[0], int(line[1:])
        if op == FORWARD:
            ship = move_ship(ship, waypoint, arg)
        else:
            waypoint = update_waypoint(waypoint, op, arg)
    return abs(ship.x) + abs(ship.y)


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