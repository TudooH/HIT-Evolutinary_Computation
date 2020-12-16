from abc import ABCMeta, abstractmethod
import random
import numpy as np


class Selection(metaclass=ABCMeta):
    @abstractmethod
    def select(self, values, rate):
        pass


class FitnessProportionateSelection(Selection):
    def select(self, values, rate):
        values = np.array(values)
        bias = values.mean() - 2 * values.std()
        tmp = np.array([max(0, values[i] - bias) for i in range(len(values))])
        values = tmp / sum(tmp)

        tot = int(len(values) * rate)
        winners = np.random.choice([i for i in range(len(values))], size=tot, p=values)
        return sorted(winners)


class TournamentSelection(Selection):
    def select(self, values, rate):
        winners = []
        while len(winners) < len(values) * rate:
            x, y = random.sample(range(len(values)), 2)
            if values[x] >= values[y]:
                winners.append(x)
            else:
                winners.append(y)
        return sorted(winners)


class ElitismSelection(Selection):
    def select(self, values, rate):
        values = {i: values[i] for i in range(len(values))}
        sorted_values = sorted(values.items(), key=lambda x: (x[1], x[0]), reverse=True)
        tot = int(len(values) * rate)
        return sorted([sorted_values[: tot][i][0] for i in range(tot)])
