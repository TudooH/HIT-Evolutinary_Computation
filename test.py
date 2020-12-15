from tsp import Tsp
from individual import Individual


if __name__ == '__main__':
    tsp = Tsp('a280')
    individual = Individual(tsp)
    for i in range(5):
        route = individual.get_route()
        dis = individual.get_dis(route)
        print(dis, route)
