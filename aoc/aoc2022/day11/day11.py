"""https://adventofcode.com/2022/day/11"""
import re
from collections import Counter, deque
from functools import reduce
from operator import mul
from os import path
from typing import Callable, Dict, Optional, Tuple


class Monkey:
    def __init__(
        self,
        id: int,
        operation: Callable[[int], int],
        test: int,
        test_true: int,
        test_false: int,
    ) -> None:
        self.id = id
        self._operation = operation
        self.test = test
        self._true = test_true
        self._false = test_false

    def inspect(
        self, worry_level: int, post_op: Optional[Callable[[int], int]] = None
    ) -> Tuple[int, int]:
        # print(worry_level)
        new = self._operation(worry_level)
        if post_op:
            new = post_op(new)
        # print(new)
        return self._true if new % self.test == 0 else self._false, new


def parse_input(inpt: str) -> Tuple[Dict[int, deque[int]], Dict[int, Monkey]]:
    pattern = re.compile(
        r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>(\d+(, )?)+)
  Operation: new = (?P<op>.+)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<true>\d+)
    If false: throw to monkey (?P<false>\d+)"""
    )
    items_dict = dict()
    monkeys = dict()
    for monkey in inpt.split("\n\n"):
        groups = pattern.match(monkey).groupdict()
        monkey_id = int(groups["id"])
        items = deque(int(n) for n in groups["items"].split(","))

        op = eval(f"lambda old: {groups['op']}")

        test = int(groups["test"])
        test_true = int(groups["true"])
        test_false = int(groups["false"])

        items_dict[monkey_id] = items
        monkeys[monkey_id] = Monkey(monkey_id, op, test, test_true, test_false)

    return items_dict, monkeys


# Part 1
def part1(inpt: str):
    items_dict, monkeys = parse_input(inpt)
    counter = Counter()
    for _ in range(20):
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            items = items_dict[m]
            while items:
                item = items.popleft()
                target, new_item = monkey.inspect(item, lambda x: x // 3)
                items_dict[target].append(new_item)
                counter[m] += 1
    return reduce(mul, [x[1] for x in counter.most_common(2)])


# Part 2
def part2(inpt: str):
    items_dict, monkeys = parse_input(inpt)
    lcm = reduce(mul, (m.test for m in monkeys.values()))
    counter = Counter()
    for _ in range(10000):
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            items = items_dict[m]
            while items:
                item = items.popleft()
                target, new_item = monkey.inspect(item, lambda x: x % lcm)
                items_dict[target].append(new_item)
                counter[m] += 1
    return reduce(mul, [x[1] for x in counter.most_common(2)])


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
