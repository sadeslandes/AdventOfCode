from os import path

ORIGINAL_SUBJECT_NUMBER = 7


def find_loop_size(subj_num, public_key):
    loop_size = 1
    while True:
        if transform(subj_num, loop_size) == public_key:
            break
        loop_size += 1
    return loop_size


def transform(subj_num, loop_size, cache=dict()):
    _mod = 20201227
    if (subj_num, loop_size - 1) in cache:
        val = (cache[(subj_num, loop_size - 1)] * subj_num) % _mod
    else:
        val = 1
        for _ in range(loop_size):
            val *= subj_num
            val = val % _mod
    cache[(subj_num, loop_size)] = val
    return val


# Part 1
def part1(inpt: str):
    card_pub, door_pub = [int(n) for n in inpt.splitlines()]
    card_loop_size = find_loop_size(ORIGINAL_SUBJECT_NUMBER, card_pub)
    door_loop_size = find_loop_size(ORIGINAL_SUBJECT_NUMBER, door_pub)
    if card_loop_size < door_loop_size:
        encryption_key = transform(door_pub, card_loop_size)
    else:
        encryption_key = transform(card_pub, door_loop_size)
    return encryption_key


# Part 2
def part2(_: str):
    return "you did it"


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
