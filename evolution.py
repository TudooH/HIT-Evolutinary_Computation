import random

from population import Population


class Evolution:
    def __init__(self, tsp, size, generation, selection, crossover, mutation, selection_rate, mutation_rate):
        self.__size = size
        self.__population = Population(tsp, size)
        self.__generation = generation
        self.__selection = selection
        self.__crossover = crossover
        self.__mutation = mutation
        self.__selection_rate = selection_rate
        self.__mutation_rate = mutation_rate
        self.__values = []
        for x in self.__population.get():
            self.__values.append(1. / x.get_dis())

    def forward(self):
        selected = self.__selection.select(self.__values, self.__selection_rate)

        offsprings = []
        while len(offsprings) < self.__size:
            x, y = random.sample(range(len(selected)), 2)
            route1 = self.__population.get(selected[x]).get_route()
            route2 = self.__population.get(selected[y]).get_route()
            cross1, cross2 = self.__crossover.crossover(route1, route2)

            rand = random.random()
            if rand <= self.__mutation_rate:
                cross1 = self.__mutation.mutate(cross1)

            rand = random.random()
            if rand <= self.__mutation_rate:
                cross2 = self.__mutation.mutate(cross2)

            offsprings.append(cross1)
            offsprings.append(cross2)

        self.__population.change(offsprings)
        self.__values = []
        for x in self.__population.get():
            self.__values.append(1. / x.get_dis())

    def get_population(self):
        return self.__population
