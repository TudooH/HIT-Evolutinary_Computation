from individual import Individual


class Population:
    def __init__(self, tsp, size):
        self.__tsp = tsp
        self.__individuals = []
        for i in range(size):
            self.__individuals.append(Individual(tsp))

    def get(self, i=None):
        if i is None:
            return self.__individuals[:]
        else:
            return self.__individuals[i]

    def change(self, offsprings):
        self.__individuals = []
        for x in offsprings:
            self.__individuals.append(Individual(self.__tsp, x))

    def min(self):
        min_dis = self.__individuals[0].get_dis()
        min_route = self.__individuals[0].get_route()
        for individual in self.__individuals:
            if individual.get_dis() < min_dis:
                min_dis = individual.get_dis()
                min_route = individual.get_route()
        return min_dis, min_route
