import gzip


class Tsp:
    def __init__(self, filename):
        with gzip.GzipFile('data/{}.tsp.gz'.format(filename)) as f:
            lines = f.read().decode().split('\n')

        self.__name = lines[0].split(':')[1][1:]
        self.__comment = lines[1].split(':')[1][1:]
        self.__type = lines[2].split(':')[1][1:]
        self.__num = int(lines[3].split(':')[1][1:])
        self.__edge_type = lines[4].split(':')[1][1:]
        self.__nodes = []
        for i in range(self.__num):
            nums = lines[i+6].split()
            self.__nodes.append([float(nums[1]), float(nums[2])])

    def get_info(self):
        return self.__name, self.__comment, self.__type, self.__num, self.__edge_type, self.__nodes
