from strategy import *
import sys


class Player():
    def __init__(self, name: str, strategy: Strategy):
        self.__name = name
        self.__strategy = strategy
        self.__wincount = 0
        self.__losecount = 0
        self.__gamecount = 0

    def __str__(self):
        return "[" + self.__name + ":" + str(self.__gamecount) + "games, " + str(self.__wincount) + "win, " + str(self.__losecount) + "lose" + "]"

    def next_hand(self) -> Hand:
        return self.__strategy.next_hand()

    def win(self) -> None:
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self) -> None:
        self.__strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self) -> None:
        self.__gamecount += 1


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py randomseed1 randomseed2")
        print("Example: python main.py 314 15")
        sys.exit()

    seed1 = int(sys.argv[1])
    seed2 = int(sys.argv[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))

    for i in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()

        if(next_hand1.is_stronger_than(next_hand2)):
            print("winner:", str(player1))
            player1.win()
            player2.lose()
        elif(next_hand2.is_stronger_than(next_hand1)):
            print("winner:" + str(player2))
            player1.lose()
            player2.win()
        else:
            print("even")
            player1.even()
            player2.even()
    print("total result:")
    print(player1)
    print(player2)


if __name__ == "__main__":
    main()
