import os
from matplotlib import pyplot as plt

from tsp import Tsp

# get result from file log

sizes = [10, 20, 50, 100]
generations = [5000, 10000, 20000]
with open('result/test1.txt', 'w') as f1:
    for dirname, _, filenames in os.walk('log/test1'):
        for filename in filenames:
            data = {}
            with open(os.path.join(dirname, filename), 'r') as f:
                ans = int(f.readline().split(', ')[1])
                f.readline()
                for size in sizes:
                    if filename == 'pr2392.txt' and size in [50, 100]:
                        continue
                    for generation in generations:
                        for solution in range(3):
                            f.readline()
                            line = f.readline().split(' ')
                            dis = [float(line[i]) for i in range(len(line)-1)]
                            final = float(f.readline())
                            dis.append(final)
                            line = f.readline().split(' ')
                            route = [int(line[i]) for i in range(len(line)-1)]
                            route.append(route[0])
                            f.readline()

                            if generation != 20000:
                                continue
                            if size == 10:
                                data[solution] = [size, final, dis, route]
                            elif final < data[solution][1]:
                                data[solution] = [size, final, dis, route]

                            filename1 = filename.split('.')[0]
                            f1.write('data: {}, generation: {}, size: {}, solution{}, ans: {}, result: {}\n'.
                                     format(filename1, generation, size, solution, ans, final))

with open('result/test2.txt', 'w') as f2:
    for dirname, _, filenames in os.walk('log/test2'):
        for filename in filenames:
            data = {}
            with open(os.path.join(dirname, filename), 'r') as f:
                ans = int(f.readline().split(', ')[1])
                f.readline()
                line = f.readline().split(' ')
                dis = [float(line[i]) for i in range(len(line)-1)]
                final = float(f.readline())
                dis.append(final)
                line = f.readline().split(' ')
                route = [int(line[i]) for i in range(len(line)-1)]
                route.append(route[0])

                filename = filename.split('.')[0]
                f2.write('data: {}, ans: {}, result: {}\n'.
                         format(filename, ans, final))
