from enum import Enum, auto

class Hand(Enum):
    pair = auto()
    flush = auto()
    high_card = auto()
    straight = auto()
