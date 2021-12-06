import re
from collections import deque, namedtuple
from os import path

Edge = namedtuple("Edge", ["name", "weight"])


def parse_input(inpt):
    p = re.compile(r"(\d) ([\w ]+) bag")
    adj_list = {}
    for line in inpt:
        sink, other = line.split(" bags contain ")
        if sink not in adj_list:
            adj_list[sink] = []
        for source in other.replace(".", "").split(", "):
            m = p.match(source)
            if m:
                source_name = m[2]
                weight = int(m[1])
                adj_list.setdefault(source_name, []).append(Edge(sink, weight))
    return adj_list


def get_visited(adj_list, start):
    visited = set()
    nxt = deque(n.name for n in adj_list[start])
    while len(nxt) > 0:
        cur = nxt.popleft()
        if cur not in visited:
            visited.add(cur)
            nxt.extend(n.name for n in adj_list[cur])
    return visited


def get_cost(adj_list, node, cost=None):
    cost = 0
    adj = adj_list[node]
    if len(adj) == 0:
        return 0
    for e in adj:
        cost += e.weight + e.weight * get_cost(adj_list, e.name)
    return cost


def reverse_edges(adj_list):
    reverse = {}
    for n in adj_list:
        if n not in reverse:
            reverse[n] = []
        for e in adj_list[n]:
            reverse.setdefault(e.name, []).append(Edge(n, e.weight))
    return reverse


# Part 1
def part1(inpt: str):
    adj_list = parse_input(inpt.splitlines())
    visited = get_visited(adj_list, "shiny gold")
    return len(visited)


# Part 2
def part2(inpt: str):
    adj_list = parse_input(inpt.splitlines())
    cost = get_cost(reverse_edges(adj_list), "shiny gold")
    return cost


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
