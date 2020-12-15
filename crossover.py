from abc import ABCMeta, abstractmethod
import random


class Crossover(metaclass=ABCMeta):
    @abstractmethod
    def crossover(self):
        pass


class OrderCrossover(Crossover):
    def __init__(self, route1, route2):
        self.__route1 = route1
        self.__route2 = route2

    def crossover(self):
        x, y = random.sample(range(len(self.__route1)), 2)
        x, y = min(x, y), max(x, y)

        cross1 = self.__route1[x: y + 1]
        cross2 = self.__route2[x: y + 1]

        offspring1 = []
        offspring2 = []
        p1, p2 = 0, 0
        for i in range(len(self.__route1)):
            if x <= i <= y:
                offspring1.append(self.__route1[i])
                offspring2.append(self.__route2[i])
                continue

            while self.__route2[p2] in cross1:
                p2 += 1
            offspring1.append(self.__route2[p2])
            p2 += 1

            while self.__route1[p1] in cross2:
                p1 += 1
            offspring2.append(self.__route1[p1])
            p1 += 1

        return offspring1, offspring2


class PMXCrossover(Crossover):
    def __init__(self, route1, route2):
        self.__route1 = route1
        self.__route2 = route2

    def crossover(self):
        x, y = random.sample(range(len(self.__route1)), 2)
        x, y = min(x, y), max(x, y)

        cross1 = self.__route1[x: y+1]
        cross2 = self.__route2[x: y+1]

        offspring1 = []
        offspring2 = []
        for i in range(len(self.__route1)):
            if x <= i <= y:
                offspring1.append(self.__route2[i])
                offspring2.append(self.__route1[i])
                continue

            tmp = self.__route1[i]
            while tmp in cross2:
                p = cross2.index(tmp)
                tmp = cross1[p]
            offspring1.append(tmp)

            tmp = self.__route2[i]
            while tmp in cross1:
                p = cross1.index(tmp)
                tmp = cross2[p]
            offspring2.append(tmp)

        return offspring1, offspring2


class CycleCrossover(Crossover):
    def __init__(self, route1, route2):
        self.__route1 = route1
        self.__route2 = route2

    def crossover(self):
        x = random.randint(0, len(self.__route1)-1)

        flag = [False] * len(self.__route1)
        flag[x] = True

        tmp = self.__route2[x]
        while tmp != self.__route1[x]:
            p = self.__route1.index(tmp)
            flag[p] = True
            tmp = self.__route2[p]

        offspring1 = []
        offspring2 = []
        for i in range(len(self.__route1)):
            if flag[i]:
                offspring1.append(self.__route1[i])
                offspring2.append(self.__route2[i])
            else:
                offspring1.append(self.__route2[i])
                offspring2.append(self.__route1[i])

        return offspring1, offspring2
