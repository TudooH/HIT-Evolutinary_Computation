import random
import math


class Individual:
    def __init__(self, tsp, set_route=None):
        _, _, _, self.__num, _, self.__nodes = tsp.get_info()

        if set_route is not None:
            self.__route = set_route[:]
        else:
            route = [i for i in range(self.__num)]
            random.shuffle(route)
            self.__route = route

        route = self.__route[:]
        route.append(route[0])
        dis = 0
        for i in range(self.__num):
            x1, y1 = self.__nodes[route[i]][0], self.__nodes[route[i]][1]
            x2, y2 = self.__nodes[route[i + 1]][0], self.__nodes[route[i + 1]][1]
            dis += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.__dis = dis

    def get_route(self):
        return self.__route[:]

    def get_dis(self):
        return self.__dis

    def change_route(self, new_route):
        self.__route = new_route

        route = self.__route[:]
        route.append(route[0])
        dis = 0
        for i in range(self.__num):
            x1, y1 = self.__nodes[route[i]][0], self.__nodes[route[i]][1]
            x2, y2 = self.__nodes[route[i + 1]][0], self.__nodes[route[i + 1]][1]
            dis += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.__dis = dis
