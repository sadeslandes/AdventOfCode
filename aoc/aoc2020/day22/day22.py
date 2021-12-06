from collections import deque
from itertools import islice
from os import path


def play_combat(p1, p2):
    d1, d2 = p1[1], p2[1]
    while len(d1) > 0 and len(d2) > 0:
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 > c2:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    return p1[0] if len(d2) == 0 else p2[0]


def count_score(deck):
    zipped = zip(range(1, len(deck) + 1), reversed(deck))
    return sum((mult * val for mult, val in zipped))


def play_recursive_combat(p1, p2):
    n1, d1 = p1
    n2, d2 = p2
    states = {n: set() for n in (n1, n2)}
    while len(d1) > 0 and len(d2) > 0:
        if tuple(d1) in states[n1] or tuple(d2) in states[n2]:
            return n1
        states[n1].add(tuple(d1))
        states[n2].add(tuple(d2))
        c1, c2 = d1.popleft(), d2.popleft()
        round_winner = None
        if c2 > len(d2) or c1 > len(d1):
            round_winner = n1 if c1 > c2 else n2
        else:
            round_winner = play_recursive_combat(
                (n1, deque(islice(d1, c1))), (n2, deque(islice(d2, c2)))
            )
        if round_winner:
            if round_winner == n1:
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)
    return n1 if len(d2) == 0 else n2


def init_players(inpt: str):
    players_raw = inpt.rstrip().split("\n\n")
    players = dict()
    for p in players_raw:
        player, *cards = p.splitlines()
        players[player] = deque(int(c) for c in cards)
    return players


# Part 1
def part1(inpt: str):
    players = init_players(inpt)
    winner = play_combat(*players.items())
    return count_score(players[winner])


# Part 2
def part2(inpt: str):
    players = init_players(inpt)
    winner = play_recursive_combat(*players.items())
    return count_score(players[winner])


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
