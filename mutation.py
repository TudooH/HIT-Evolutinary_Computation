import random
from abc import ABCMeta, abstractmethod


class Mutation(metaclass=ABCMeta):
    @abstractmethod
    def mutate(self, route):
        pass


class Insert(Mutation):
    def mutate(self, route):
        x, y = random.sample(range(len(route)), 2)
        x, y = min(x, y), max(x, y)
        tmp = [route[i] if i <= x or i > y else route[i-1] for i in range(len(route))]
        tmp[x+1] = route[y]
        return tmp


class Swap(Mutation):
    def mutate(self, route):
        x, y = random.sample(range(len(route)), 2)
        route[x], route[y] = route[y], route[x]
        return route


class Inversion(Mutation):
    def mutate(self, route):
        x, y = random.sample(range(len(route)), 2)
        x, y = min(x, y), max(x, y)
        return [route[i] if i < x or i > y else route[x+y-i] for i in range(len(route))]


class Scramble(Mutation):
    def mutate(self, route):
        tot = random.randint(1, len(route))
        nums = random.sample(range(len(route)), tot)
        rand = nums[:]
        random.shuffle(rand)
        return [route[i] if route[i] not in nums else rand[nums.index(route[i])] for i in range(len(route))]
