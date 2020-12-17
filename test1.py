import time

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
ans = [426, 538, 629, 675, 21282, 20749, 21294, 14379, 50778, 378032]

selections = [FitnessProportionateSelection(), TournamentSelection(), ElitismSelection()]
crossovers = [OrderCrossover(), PMXCrossover(), CycleCrossover()]
mutations = [Insert(), Swap(), Inversion(), Scramble()]
solutions = [[1, 1, 2], [1, 2, 2], [2, 1, 2]]

for i, filename in enumerate(filenames):
    tsp = Tsp(filename)
    print(filename, ans[i])
    with open('log/test1/{}.txt'.format(filename), 'w') as f:
        start = time.time()

        f.write('{}, {}\n\n'.format(filename, ans[i]))
        for size in sizes:
            for generation in generations:
                for solution in solutions:
                    selection = selections[solution[0]]
                    crossover = crossovers[solution[1]]
                    mutation = mutations[solution[2]]
                    evolution = Evolution(tsp, size, generation, selection, crossover,
                                          mutation, select_rate, mutation_rate)
                    f.write('size: {}, generation: {}, selection: {}, crossover: {}, mutation: {}\n'.
                            format(size, generation, solution[0], solution[1], solution[2]))
                    print('size: {}, generation: {}, selection: {}, crossover: {}, mutation: {}'.
                          format(size, generation, solution[0], solution[1], solution[2]))

                    dis_log = []
                    for g in range(generation):
                        evolution.forward()
                        min_dis, _ = evolution.get_population().min()
                        if g % 1000 == 0:
                            dis_log.append(min_dis)
                    for x in dis_log:
                        f.write('{} '.format(x))
                    f.write('\n')

                    dis, route = evolution.get_population().min()
                    f.write('{}\n'.format(dis))
                    for x in route:
                        f.write('{} '.format(x))
                    f.write('\n\n')

        end = time.time()
        f.write('time: {}'.format(end-start))
