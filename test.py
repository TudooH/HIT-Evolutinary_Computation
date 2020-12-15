from tsp import Tsp
from individual import Individual


if __name__ == '__main__':
    tsp = Tsp('a280')
    individual = Individual(tsp)
    for i in range(5):
        print(individual.get_random_result())
