"""https://adventofcode.com/2021/day/14"""
from collections import Counter
from os import path


class Polymer:
    def __init__(self, template: str, rules: dict[str, str]) -> None:
        # original polymer
        self._template = template
        # rules for inseting element into polymer
        self._insertion_map = rules
        # helper for mapping an element pair to the resulting pairs after insertion
        self._pair_map = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}
        # counter of elements in polymer
        self._counter = Counter(template)

        # pairs to evaluate in next step
        self._evaluate: Counter[str] = None

    @property
    def template(self):
        return self._template

    @property
    def counter(self):
        return self._counter

    def step(self):
        if not self._evaluate:
            # use initial pairs
            self._evaluate = Counter(
                self._template[s - 1 : s + 1] for s in range(1, len(self._template))
            )
        else:
            tmp_counter = Counter()
            for pair, count in self._evaluate.items():
                tmp_counter.update(
                    {new_pair: count for new_pair in self._pair_map[pair]}
                )
            self._evaluate = tmp_counter
        # update counter
        for pair, count in self._evaluate.items():
            self.counter.update({self._insertion_map[pair]: count})


def parse_input(inpt: str) -> tuple[str, dict[str, str]]:
    template, _, *rules = inpt.splitlines()
    split_rules = (r.split(" -> ") for r in rules)
    insertions = {k: v for k, v in split_rules}
    return template, insertions


# Part 1
def part1(inpt: str):
    template, rules = parse_input(inpt)
    poly = Polymer(template, rules)
    for _ in range(10):
        poly.step()
    counter = poly.counter
    return max(counter.values()) - min(counter.values())


# Part 2
def part2(inpt: str):
    template, rules = parse_input(inpt)
    poly = Polymer(template, rules)
    for _ in range(40):
        poly.step()
    counter = poly.counter
    return max(counter.values()) - min(counter.values())


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
