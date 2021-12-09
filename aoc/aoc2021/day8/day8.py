"""https://adventofcode.com/2021/day/8"""
from os import path
from typing import Dict, List


def build_signal_map(input_signals: List[frozenset]) -> Dict[frozenset, str]:
    """Returns mapping from input signal to display value"""
    signal_map: Dict[frozenset, str] = dict()  # mapping from input signal (as a set) -> display value (as a str)
    display_map: Dict[str, frozenset] = dict()  # reverse mapping of signal_map
    unknown_signals = set(input_signals)
    # collection of display value and a rule for determining which signal corresponds with the display value
    # keep in mind that s and display_map values are sets and these are set operations
    rules = [
        ("1", lambda s: len(s) == 2),
        ("4", lambda s: len(s) == 4),
        ("7", lambda s: len(s) == 3),
        ("8", lambda s: len(s) == 7),
        ("9", lambda s: len(s) == 6 and s > (display_map["4"] | display_map["7"])),
        ("6", lambda s: len(s) == 6 and s > (display_map["8"] - display_map["1"])),
        ("0", lambda s: len(s) == 6),  # last remaining signal with 6 segments
        ("5", lambda s: s > (display_map["9"] - display_map["1"])),
        ("3", lambda s: s > ((display_map["9"] - display_map["4"]) | display_map["1"])),
        ("2", lambda _: True),  # last remaining signal
    ]
    # evaluate rules
    for display, rule in rules:
        signal = next(s for s in unknown_signals if rule(s))
        signal_map[signal] = display
        display_map[display] = signal
        unknown_signals.remove(signal)
    return signal_map


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    counter = 0
    unique_digit_len = {2, 3, 4, 7}  # corresponds with # of segments used to display 1, 7, 4, 8 respectively
    for line in inpt_lines:
        _, output_values = line.split("|")
        counter += len([v for v in output_values.strip().split() if len(v) in unique_digit_len])
    return counter


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    result = 0
    for line in inpt_lines:
        input_signals, output_values = ([frozenset(s) for s in p.strip().split()] for p in line.split("|"))
        decoder = build_signal_map(input_signals)
        result += int(''.join(decoder[v] for v in output_values))
    return result


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
