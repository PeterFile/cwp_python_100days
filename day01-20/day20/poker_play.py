import random
from enum import Enum


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    """
    魔术方法__lt__对应<运算符，魔术方法__gt__对应>运算符，魔术方法__le__对应<=运算符，__ge__对应>=运算符，__eq__对应==运算符，__ne__对应!=运算符。
    """
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)
print(card2)

class Poker:
    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)

poker = Poker()
print(poker.cards)
poker.shuffle()
print(poker.cards)

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# 将牌轮流发到每个玩家手上每人13张牌
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
# 玩家整理手上的牌输出名字和手牌
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)

