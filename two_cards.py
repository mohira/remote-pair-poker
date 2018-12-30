from typing import List

from card import Card
from hand import Hand
from rank import Rank
from suit import Suit


class TwoCards:
    def __init__(self, cards: List[Card]):
        self.card1 = cards[0]
        self.card2 = cards[1]

    @property
    def hand(self) -> Hand:
        if self.is_pair():
            return Hand.pair

        if self.is_straight():
            return Hand.straight

        if self.is_flush():
            return Hand.flush
        
        return Hand.high_card

    def is_pair(self):
        return self.card1.rank == self.card2.rank

    def is_straight(self):
        # 連続している
        # 文字コードの差分
        # 整数型に変換して差分
        pass

    def is_flush(self):
        return self.card1.suit == self.card2.suit
