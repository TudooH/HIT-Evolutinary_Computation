from tsp import Tsp
from selection import TournamentSelection
from crossover import CycleCrossover
from mutation import Inversion
from evolution import Evolution


select_rate = 0.5
mutation_rate = 0.1
size = 50
generation = 10000
filenames = ['eil51', 'eil76', 'eil101', 'st70', 'kroA100', 'kroC100', 'kroD100', 'lin105', 'pcb442', 'pr2392']
ans = [426, 538, 629, 675, 21282, 20749, 21294, 14379, 50778, 378032]

solutions = [TournamentSelection(), CycleCrossover(), Inversion()]

for i, filename in enumerate(filenames):
    tsp = Tsp(filename)
    print(filename, ans[i])
    with open('log/test2/{}.txt'.format(filename), 'w') as f:
        f.write('{}, {}\n\n'.format(filename, ans[i]))
        selection = solutions[0]
        crossover = solutions[1]
        mutation = solutions[2]
        evolution = Evolution(tsp, size, generation, selection, crossover,
                              mutation, select_rate, mutation_rate)

        dis_log = []
        for g in range(generation):
            evolution.forward()
            min_dis, _ = evolution.get_population().min()
            if g % 100 == 0:
                dis_log.append(min_dis)
            if g % 1000 == 0:
                print(g, min_dis)
        for x in dis_log:
            f.write('{} '.format(x))
        f.write('\n')

        dis, route = evolution.get_population().min()
        f.write('{}\n'.format(dis))
        for x in route:
            f.write('{} '.format(x))
        f.write('\n\n')
