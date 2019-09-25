# from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
import random
from typing import NewType


@dataclass
class HandValueConst():
    HANDVALUE_GUU: int = 0
    HANDVALUE_CHOKI: int = 1
    HANDVALUE_PAA: int = 2
    string_name: list = field(default_factory=['グー', 'チョキ', 'パー'])


class Hand():
    def __init__(self, handvalue: int):
        self.handvalue: int = handvalue

    def __str__(self):
        return HandValueConst.string_name[self.handvalue]

    # def get_hand(self, handvalue: int) -> Hand:
    #   return Hand(handvalue)

    def is_stronger_than(self, h: 'Hand') -> bool:
        return self.__fight(h) == 1

    def is_weaker_than(self, h: 'Hand') -> bool:
        return self.__fight(h) == -1

    def __fight(self, h: 'Hand') -> 'Hand':
        if(self.handvalue == h):
            return 0
        elif((self.handvalue + 1) % 3 == h.handvalue):
            return 1
        else:
            return -1


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self) -> Hand:
        pass

    @abstractmethod
    def study(self) -> bool:
        pass


class WinningStrategy(Strategy):
    def __init__(self, seed: int):
        # self.__random = random.seed(seed)#randomのインスタンスを持ちたい
        self.__seed = seed
        self.__won = False
        self.__prev_hand = 0  # たぶん数値で手を決めている

    def next_hand(self) -> Hand:
        random.seed(self.__seed)
        if(not self.__won):  # 負けたら手をかえる、勝っていたら前の手をそのまま出す
            self.__prev_hand = Hand(random.randint(0, 3))  # 一旦新しくインスタンス作ってよぶ
        return self.__prev_hand

    def study(self, win: bool) -> None:
        self.__won = win


class ProbStrategy(Strategy):
    # history[前回の手][今回のて]の勝率をもつ
    def __init__(self, seed: int):
        self.__seed = seed  # randomのインスタンスを持ちたい
        self.__prev_hand_value = 0
        self.__current_hand_value = 0
        self.__history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def next_hand(self) -> Hand:
        random.seed(self.__seed)
        __bet = random.randint(0, self.__get_sum(self.__current_hand_value))
        __hand_value = 0  # 次に出す手

        if(__bet < self.__history[self.__current_hand_value][0]):
            __hand_value = 0
        elif(__bet < self.__history[self.__current_hand_value][0] + self.__history[self.__current_hand_value][1]):
            __hand_value = 1
        else:
            __hand_value = 2

        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = __hand_value
        return Hand(__hand_value)  # 一旦新しくインスタンス作ってよぶ

    def __get_sum(self, hv: int) -> int:
        __sum = 0
        for i in range(3):
            __sum += self.__history[hv][i]
        return __sum

    def study(self, win: bool) -> None:
        if(win):
            self.__history[self.__prev_hand_value][self.__current_hand_value] = self.__history[self.__prev_hand_value][self.__current_hand_value]+1
        else:
            self.__history[self.__prev_hand_value][(
                self.__current_hand_value + 1) % 3] = self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] + 1
            self.__history[self.__prev_hand_value][(
                self.__current_hand_value + 2) % 3] = self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] + 1
