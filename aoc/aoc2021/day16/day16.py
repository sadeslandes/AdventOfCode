"""https://adventofcode.com/2021/day/16"""
from os import path

from aoc.aoc2021.day16.packets import Packet, PacketFactory


def hex_to_binary(hex: str) -> str:
    return bin(int("1" + hex, 16))[3:]


def check_sum(packet: Packet) -> int:
    if not packet.InnerPackets:
        return packet.Version
    return packet.Version + sum(check_sum(p) for p in packet.InnerPackets)


# Part 1
def part1(inpt: str):
    binary = hex_to_binary(inpt.rstrip())
    packet = PacketFactory.parse_packet(binary)
    return check_sum(packet)


# Part 2
def part2(inpt: str):
    binary = hex_to_binary(inpt.rstrip())
    packet = PacketFactory.parse_packet(binary)
    return packet.evaluate()


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
