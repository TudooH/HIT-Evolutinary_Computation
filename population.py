from abc import ABCMeta, abstractmethod


class Population(metaclass=ABCMeta):
    @abstractmethod
    def get_route(self):
        pass

    @abstractmethod
    def get_dis(self, route):
        pass
