from os import path


def move(cups, cur):
    rem1 = cups[cur]
    rem2 = cups[rem1]
    rem3 = cups[rem2]
    rest = cups[rem3]

    dest = cur
    # find destination
    while True:
        dest -= 1
        if dest in (rem1, rem2, rem3):
            continue
        if dest == 0:
            dest = len(cups)
            continue
        break

    cups[cur] = rest
    cups[rem3] = cups[dest]
    cups[dest] = rem1

    return rest


def make_cups_list(inpt):
    cups = [0] * (len(inpt) + 1)
    idx = 0
    for n in inpt:
        cups[idx] = n
        idx = n
    cups[inpt[-1]] = inpt[0]
    return cups


def iterate_cups(cups):
    idx = 0
    for _ in range(len(cups)-1):
        yield cups[idx]
        idx = cups[idx]


# Part 1
def part1(inpt: str):
    # [int(n) for n in f.readline().rstrip()]
    nums = [int(n) for n in inpt.rstrip()]
    cups = make_cups_list(nums)
    current = cups[0]
    for _ in range(100):
        current = move(cups, current)

    ordered_cups = list(iterate_cups(cups))
    start = ordered_cups.index(1)
    labels = ""
    for offset in range(1, len(ordered_cups)):
        idx = (start + offset) % len(ordered_cups)
        labels += str(ordered_cups[idx])
    return labels


# Part 2
def part2(inpt: str):
    nums = [int(n) for n in inpt.rstrip()]
    # extend input
    nums.extend(n for n in range(max(nums) + 1, int(1e6 + 1)))

    cups = make_cups_list(nums)
    current = cups[0]
    for _ in range(int(1e7)):
        current = move(cups, current)

    ordered_cups = list(iterate_cups(cups))
    start = ordered_cups.index(1)
    val = 1
    for offset in range(1, 3):
        idx = (start + offset) % len(ordered_cups)
        val *= ordered_cups[idx]
    return val


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
