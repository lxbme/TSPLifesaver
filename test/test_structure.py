import unittest

from TSPLifesaver.structure import *


class TestStructure(unittest.TestCase):
    def test_point(self):
        self.point_1 = PointWithEuclideanDistance([1, 1, 1, 1], name="test name 1")
        self.point_2 = PointWithEuclideanDistance([2, 2, 2, 2], name="test name 2")

        self.assertEqual(self.point_1.distance_to(self.point_2), 2)
        self.assertEqual(self.point_1.distance_to([2, 2, 2, 2]), 2)

        self.assertEqual(len(self.point_1), 4)
        self.assertEqual(self.point_1[0], 1)

    def test_route(self):
        self.points = [PointWithEuclideanDistance(i, i) for i in [[1, 1], [2, 2], [3, 3]]]
        self.route = BasicRoute(self.points, name="test route")
        self.assertEqual(self.route.distance(), sqrt(2)*4)
