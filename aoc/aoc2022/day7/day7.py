"""https://adventofcode.com/2022/day/7"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from os import path
from typing import Dict, Iterator, List, Optional, Union


@dataclass
class File:
    size: int
    name: str

    def __repr__(self) -> str:
        return f"(file {self.name}, size={self.size})"


class Directory:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.children: Dict[str, Union[File, Directory]] = dict()
        self.parent: Optional[Directory] = None

    def __repr__(self) -> str:
        return f"(dir {self.name}, children={len(self.children)})"

    def add_child(self, child: Union[File, Directory]):
        self.children[child.name] = child
        if isinstance(child, Directory):
            child.parent = self

    def traverse_dirs(self) -> Iterator[Directory]:
        yield self
        for c in self.children.values():
            if isinstance(c, File):
                continue
            else:
                yield from c.traverse_dirs()

    @property
    @lru_cache
    def size(self) -> int:
        return sum(c.size for c in self.children.values())


def build_fs(output: List[str]) -> Directory:
    root = Directory("/")
    current = root
    for line in output:
        parsed = line.split()
        if parsed[0] == "$":
            # command
            if parsed[1] == "cd":
                if parsed[2] == "..":
                    current = current.parent
                elif parsed[2] == "/":
                    continue
                else:
                    current = current.children[parsed[2]]
        elif parsed[0] == "dir":
            # directory
            current.add_child(Directory(parsed[1]))
        else:
            # file
            current.add_child(File(int(parsed[0]), parsed[1]))
    return root


# Part 1
def part1(inpt: str):
    fs = build_fs(inpt.splitlines())
    max_size = 100000
    return sum(x.size for x in fs.traverse_dirs() if x.size <= max_size)


# Part 2
def part2(inpt: str):
    fs = build_fs(inpt.splitlines())
    total_size = 70000000
    required_size = 30000000
    current_size = total_size - fs.size
    return min(
        x.size for x in fs.traverse_dirs() if current_size + x.size > required_size
    )


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
