"""https://adventofcode.com/2021/day/4"""
from os import path
from dataclasses import dataclass
from typing import List


@dataclass
class BingoNumber:
    number: int
    is_marked: bool = False


Board = List[List[BingoNumber]]


def is_bingo(board: Board):
    # check rows
    for row in board:
        if all([c.is_marked for c in row]):
            return True
    # check cols
    for col_num in range(len(board[0])):
        if all([row[col_num].is_marked for row in board]):
            return True
    return False


def play_bingo(nums: List[int], boards: List[Board]):
    completed_boards = set()
    for num in nums:
        for board in boards:
            if id(board) in completed_boards:
                # skip completed boards
                continue
            for row in board:
                if id(board) in completed_boards:
                    # board was just completed
                    break
                for col in row:
                    if col.number == num:
                        col.is_marked = True
                        # check if won
                        if is_bingo(board):
                            completed_boards.add(id(board))
                            yield (board, num)
                            break


def get_score(board: Board, winning_num: int):
    unmarked = (n.number for row in board for n in row if not n.is_marked)
    return winning_num * sum(unmarked)


# Part 1
def part1(inpt: str):
    nums, *boards = inpt.split('\n\n')
    nums = map(int, nums.split(','))
    boards = [[[BingoNumber(int(n)) for n in row.split()] for row in board.splitlines()] for board in boards]
    winning_board, winning_num = next(play_bingo(nums, boards))
    return get_score(winning_board, winning_num)


# Part 2
def part2(inpt: str):
    nums, *boards = inpt.split('\n\n')
    nums = map(int, nums.split(','))
    boards = [[[BingoNumber(int(n)) for n in row.split()] for row in board.splitlines()] for board in boards]
    winning_board, winning_num = list(play_bingo(nums, boards))[-1]
    return get_score(winning_board, winning_num)


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
