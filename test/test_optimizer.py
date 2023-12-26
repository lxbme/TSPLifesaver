import unittest

from TSPLifesaver.optimizer import *
from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance


class TestStructure(unittest.TestCase):

    def test_SimulatedAnnealing(self):
        self.points = [PointWithEuclideanDistance(i) for i in
                       [[565, 575], [25, 185], [345, 750], [945, 685], [845, 655], [880, 660],
                        [25, 230], [525, 1000], [580, 1175], [650, 1130], [1605, 620], [1220, 580], [1465, 200],
                        [1530, 5],
                        [845, 680], [725, 370]]]
        self.route = BasicRoute(self.points, name="test route")
        optimizer = SimulatedAnnealing(self.route, 10000, 0.003, 1)
        self.route = optimizer.optimize()
        print("\n")
        print(self.route.distance())

    def test_ExhaustiveIndexing(self):
        self.points = [PointWithEuclideanDistance(i) for i in
                       [[565, 575], [25, 185], [345, 750], [945, 685], [845, 655], [880, 660],
                        [25, 230], [525, 1000]]]
        self.route = BasicRoute(self.points, name="test route")
        optimizer = ExhaustiveIndexing(self.route)
        self.route = optimizer.optimize()

        print("\n")
        print(self.route.distance())
