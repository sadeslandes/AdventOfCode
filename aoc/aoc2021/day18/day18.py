"""https://adventofcode.com/2021/day/18"""
from __future__ import annotations

import operator
from dataclasses import dataclass
from functools import reduce
from math import ceil, floor
from os import path


class Tree:
    _o_bracket = "["
    _c_bracket = "]"
    _separator = ","

    @dataclass
    class Node:
        value: int = None
        left: Tree.Node = None
        right: Tree.Node = None
        parent: Tree.Node = None
        depth: int = 0

        @property
        def is_leaf(self) -> bool:
            return self.left is None and self.right is None

        def __str__(self) -> str:
            if self.is_leaf:
                return str(self.value)
            else:
                return f"[{str(self.left)},{str(self.right)}]"

        def __eq__(self, _o: object) -> bool:
            return id(self) == id(_o)

    @staticmethod
    def parse(expr: str) -> Tree:
        stack = list()
        node = None
        for c in expr:
            if c == Tree._o_bracket:
                stack.append([Tree.Node(depth=len(stack)), True])
            elif c.isdigit():
                node, left = stack[-1]
                if left:
                    node.left = Tree.Node(value=int(c), parent=node, depth=len(stack))
                else:
                    node.right = Tree.Node(value=int(c), parent=node, depth=len(stack))
            elif c == Tree._separator:
                stack[-1][-1] = False
            elif c == Tree._c_bracket:
                node, _ = stack.pop()
                if stack:
                    p_node, p_left = stack[-1]
                    node.parent = p_node
                    if p_left:
                        p_node.left = node
                    else:
                        p_node.right = node
        return Tree(root=node)

    def __init__(self, root: Node) -> None:
        self.root = root

    def __str__(self) -> str:
        return str(self.root)

    def __add__(self, other: Tree):
        # Copies aren't being made so this has side effects on self and other
        new_node = Tree.Node(value=None, left=self.root, right=other.root, depth=-1)
        new_node.left.parent = new_node.right.parent = new_node
        new = Tree(new_node)
        # increment node depths
        new._increment_depth()
        new._reduce()
        return new

    def _list_leaves(self) -> list[Tree.Node]:
        nodes = []
        Tree._leaves_inner(self.root, nodes)
        return nodes

    @staticmethod
    def _leaves_inner(node: Tree.Node, lst: list[Tree.Node]) -> list[Tree.Node]:
        if node.is_leaf:
            lst.append(node)
        else:
            Tree._leaves_inner(node.left, lst)
            Tree._leaves_inner(node.right, lst)

    def _increment_depth(self, node: Tree.Node = None):
        if node is None:
            node = self.root
        node.depth += 1
        if node.is_leaf:
            return
        else:
            self._increment_depth(node.left)
            self._increment_depth(node.right)

    def _explode(self) -> bool:
        parents = set()
        leaves = self._list_leaves()
        for leaf in leaves:
            parent = leaf.parent
            if id(parent) in parents:
                continue
            parents.add(id(parent))
            if parent.depth < 4:
                continue
            # store references to leaves
            left = parent.left
            right = parent.right

            # turn parent into leaf
            parent.left = None
            parent.right = None
            parent.value = 0

            # search left leaves
            if (idx := leaves.index(left)) != 0:
                leaves[idx - 1].value += left.value
            # search right leaves
            if (idx := leaves.index(right)) != len(leaves) - 1:
                leaves[idx + 1].value += right.value
            return True
        return False

    def _split(self) -> bool:
        for leaf in self._list_leaves():
            if (val := leaf.value) > 9:
                leaf.left = Tree.Node(value=floor(val / 2))
                leaf.right = Tree.Node(value=ceil(val / 2))
                leaf.left.parent = leaf.right.parent = leaf
                leaf.left.depth = leaf.right.depth = leaf.depth + 1
                leaf.value = None
                return True
        return False

    def _reduce(self):
        while True:
            if self._explode():
                continue
            if self._split():
                continue
            break

    def get_magnitude(self):
        return self._get_magnitude_inner(self.root)

    def _get_magnitude_inner(self, node: Tree.Node) -> int:
        if node.is_leaf:
            return node.value
        return (3 * self._get_magnitude_inner(node.left)) + (
            2 * self._get_magnitude_inner(node.right)
        )


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    return reduce(operator.add, map(Tree.parse, inpt_lines)).get_magnitude()


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    magnitude = 0
    for i in range(len(inpt_lines)):
        for j in range(len(inpt_lines)):
            total = Tree.parse(inpt_lines[i]) + Tree.parse(inpt_lines[j])
            magnitude = max(magnitude, total.get_magnitude())
    return magnitude


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
