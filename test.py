from tsp import Tsp
from selection import FitnessProportionateSelection, TournamentSelection, ElitismSelection
from crossover import OrderCrossover, PMXCrossover, CycleCrossover
from mutation import Insert, Swap, Inversion, Scramble
from evolution import Evolution


select_rate = 0.5
mutation_rate = 0.1
sizes = [10, 20, 50, 100]
generations = [5000, 10000, 20000]
filenames = ['eil51', 'eil76', 'eil101', 'st70', 'kroA100', 'kroC100', 'kroD100', 'lin105', 'pcb442', 'pr2392']
solutions = [[FitnessProportionateSelection(), OrderCrossover(), Insert()],
             [TournamentSelection(), PMXCrossover(), Swap()],
             [ElitismSelection(), CycleCrossover(), Inversion()]]

for filename in filenames:
    tsp = Tsp(filename)
    for size in sizes:
        for generation in generations:
            for solution in solutions:
                evolution = Evolution(tsp, size, generation, solution[0], solution[1], solution[2],
                                      select_rate, mutation_rate)
                for i in range(generation):
                    evolution.forward()
                    min_dis, _ = evolution.get_population().min()

                print(filename, size, generation, solution, min_dis)
