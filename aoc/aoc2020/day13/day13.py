from itertools import count
from os import path


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    earliest = int(inpt_lines[0])
    ids = [int(_id) for _id in inpt_lines[1].split(",") if _id != "x"]
    timestamp = earliest
    while True:
        for _id in ids:
            if timestamp % _id == 0:
                return (timestamp - earliest) * _id
        timestamp += 1


# Part 2
# noqa: E501 - https://old.reddit.com/r/adventofcode/comments/kc60ri/2020_day_13_can_anyone_give_me_a_hint_for_part_2/gfnnfm3/ for hint
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    id_enumerator = enumerate(inpt_lines[1].split(","))
    ids = [(int(_id), i) for i, _id in id_enumerator if _id != "x"]
    # consider only one bus
    # all busses departed at 0 so this is the earliest timestamp for one bus
    # additional departure times for one bus can be found by repeatedly adding
    # its id
    t = 0
    w = ids[0][0]

    # consider the other busses
    for _id, offset in ids[1:]:
        # increment t by w until we find a value for t that satisfies
        # conditions for the bus under consideration
        for n in count(t, w):
            if (n + offset) % _id == 0:
                # update t and w
                # w is actually lcm of bus ids being considered
                # but since ids are all prime we can just multiply
                t = n
                w *= _id
                break
    return t


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
