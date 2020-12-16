from abc import ABCMeta, abstractmethod
import random


class Selection(metaclass=ABCMeta):
    @abstractmethod
    def select(self):
        pass


class TournamentSelection(Selection):
    def __init__(self, values, rate):
        self.__values = values
        self.__rate = rate

    def select(self):
        winners = []
        while len(winners) < len(self.__values) * self.__rate:
            x, y = random.sample(range(len(self.__values)), 2)
            if self.__values[x] >= self.__values[y]:
                winners.append(x)
            else:
                winners.append(y)
        return sorted(winners)


class ElitismSelection(Selection):
    def __init__(self, values, rate):
        self.__values = {i: values[i] for i in range(len(values))}
        self.__rate = rate

    def select(self):
        sorted_values = sorted(self.__values.items(), key=lambda x: (x[1], x[0]), reverse=True)
        tot = int(len(self.__values) * self.__rate)
        return sorted([sorted_values[: tot][i][0] for i in range(tot)])
