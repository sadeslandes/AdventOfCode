from __future__ import annotations

import operator
from abc import ABC, abstractmethod
from enum import IntEnum
from functools import reduce

__all__ = ["Packet", "PacketFactory"]


class PacketType(IntEnum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


class Packet(ABC):
    """Abstract base class for all packets"""

    def __init__(self, version: int, type: PacketType, length: int) -> None:
        self._version = version
        self._type = type
        self._length = length + 6  # to account for header bits

    @property
    def Version(self) -> int:
        return self._version

    @property
    def Type(self) -> PacketType:
        return self._type

    @property
    @abstractmethod
    def InnerPackets(self) -> list[Packet]:
        pass

    @abstractmethod
    def evaluate(self) -> int:
        pass


class LiteralPacket(Packet):
    """Literal packet class"""

    def __init__(self, version: int, binary: str) -> None:
        self._value, length = self._parse_value(binary)
        super().__init__(version, PacketType.LITERAL, length)

    @property
    def Value(self):
        return self._value

    @property
    def InnerPackets(self) -> list[Packet]:
        return None

    def evaluate(self) -> int:
        return self.Value

    @staticmethod
    def _parse_value(binary: str) -> tuple[int, int]:
        value_str = ""
        length = len(binary)
        for i in range(0, length, 5):
            chunk = binary[i : i + 5]
            control, val = int(chunk[:1]), chunk[1:]
            value_str += val
            if control == 0:
                length = i + 5
                break
        return int(value_str, 2), min(length, len(binary))


class OperatorPacket(Packet, ABC):
    """Abstract base class for operator packets"""

    class LengthType(IntEnum):
        LENGTH = 0
        NUMBER = 1

    def __init__(self, version: int, binary: str, type: PacketType) -> None:
        self._inner_packets, length = self._parse_packets(binary)
        super().__init__(version, type, length)

    @property
    def Value(self):
        return self._value

    @property
    def InnerPackets(self) -> list[Packet]:
        return self._inner_packets

    def evaluate(self) -> int:
        pass

    @staticmethod
    def _parse_packets(binary: str) -> tuple[list[Packet], int]:
        length_type_id = int(binary[:1])
        if length_type_id == OperatorPacket.LengthType.LENGTH:
            packets, length = OperatorPacket._parse_by_length(binary[1:])
        else:
            packets, length = OperatorPacket._parse_by_number(binary[1:])
        return packets, length + 1  # account for length type bit

    @staticmethod
    def _parse_by_length(binary: str) -> tuple[list[Packet], int]:
        packets = []
        segment_len = 15
        max_length, binary = int(binary[:segment_len], 2), binary[segment_len:]
        # parse inner packets until expected len is reached
        length = 0
        while length < max_length:
            p = PacketFactory.parse_packet(binary)
            packets.append(p)
            p_len = p._length
            length += p_len
            binary = binary[p_len:]
        assert length == max_length
        return packets, length + segment_len  # account for length type segment

    @staticmethod
    def _parse_by_number(binary: str) -> tuple[list[Packet], int]:
        packets = []
        segment_len = 11
        num_packets, binary = int(binary[:segment_len], 2), binary[segment_len:]
        # parse inner packets until expected len is reached
        length = 0
        for _ in range(num_packets):
            p = PacketFactory.parse_packet(binary)
            packets.append(p)
            p_len = p._length
            length += p_len
            binary = binary[p_len:]
        return packets, length + segment_len  # account for length type segment


class SumPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.SUM)

    def evaluate(self) -> int:
        """Sums values of inner packets"""
        return sum(p.evaluate() for p in self.InnerPackets)


class ProductPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.PRODUCT)

    def evaluate(self) -> int:
        """Multiplies values of inner packets"""
        return reduce(operator.mul, (p.evaluate() for p in self.InnerPackets))


class MinPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.MIN)

    def evaluate(self) -> int:
        return min(p.evaluate() for p in self.InnerPackets)


class MaxPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.MAX)

    def evaluate(self) -> int:
        return max(p.evaluate() for p in self.InnerPackets)


class GTPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.GT)
        assert len(self.InnerPackets) == 2

    def evaluate(self) -> int:
        return (
            1
            if self.InnerPackets[0].evaluate() > self.InnerPackets[1].evaluate()
            else 0
        )


class LTPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.LT)
        assert len(self.InnerPackets) == 2

    def evaluate(self) -> int:
        return (
            1
            if self.InnerPackets[0].evaluate() < self.InnerPackets[1].evaluate()
            else 0
        )


class EQPacket(OperatorPacket):
    def __init__(self, version: int, binary: str) -> None:
        super().__init__(version, binary, PacketType.EQ)
        assert len(self.InnerPackets) == 2

    def evaluate(self) -> int:
        return (
            1
            if self.InnerPackets[0].evaluate() == self.InnerPackets[1].evaluate()
            else 0
        )


class PacketFactory:
    packet_map = {
        PacketType.SUM: SumPacket,
        PacketType.PRODUCT: ProductPacket,
        PacketType.MIN: MinPacket,
        PacketType.MAX: MaxPacket,
        PacketType.LITERAL: LiteralPacket,
        PacketType.GT: GTPacket,
        PacketType.LT: LTPacket,
        PacketType.EQ: EQPacket,
    }

    @staticmethod
    def parse_packet(binary: str) -> Packet:
        version, binary = int(binary[:3], 2), binary[3:]
        type_id, binary = int(binary[:3], 2), binary[3:]
        return PacketFactory.packet_map[type_id](version, binary)
