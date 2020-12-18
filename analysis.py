import os
from matplotlib import pyplot as plt

from tsp import Tsp


sizes = [10, 20, 50, 100]
generations = [5000, 10000, 20000]

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

            filename = filename.split('.')[0]

            plt.title('data: {}, ans: {}'.format(filename, ans))
            plt.plot([0, 20000], [ans, ans], label='ans')
            plt.plot([i * 1000 for i in range(21)], data[0][2],
                     label='solution1(size={}): {}'.format(data[0][0], int(data[0][1])))
            plt.plot([i * 1000 for i in range(21)], data[1][2],
                     label='solution2(size={}): {}'.format(data[1][0], int(data[1][1])))
            plt.plot([i * 1000 for i in range(21)], data[2][2],
                     label='solution3(size={}): {}'.format(data[2][0], int(data[2][1])))
            plt.legend()
            plt.savefig('img/test1/{}.png'.format(filename))
            plt.show()

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
            tsp = Tsp(filename)
            nodes = tsp.get_nodes()
            plt.title('data: {}, ans: {}, final: {}'.format(filename, ans, int(final)))
            plt.scatter([nodes[i][0] for i in range(len(nodes))], [nodes[i][1] for i in range(len(nodes))], color='r')
            plt.plot([nodes[route[i]][0] for i in range(len(nodes)+1)],
                     [nodes[route[i]][1] for i in range(len(nodes)+1)],
                     color='b', linewidth=0.5)
            plt.savefig('img/test2/{}.png'.format(filename))
            plt.show()
