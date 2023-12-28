from typing import List, Any, MutableSequence, Sequence
from math import sqrt

from TSPLifesaver.abc import AbstractRoute, AbstractPoint


class BasicPoint(AbstractPoint):
    def __init__(self, pos: MutableSequence, name: Any = None):
        self.pos = pos
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __getitem__(self, item):
        return self.pos[item]

    def __setitem__(self, item, value):
        self.pos[item] = value

    def __delitem__(self, item):
        del self.pos[item]

    def __len__(self):
        return len(self.pos)

    def __str__(self):
        return str(self.name) + f"({str(self.pos)})"

    def distance_to(self, other: MutableSequence):
        """
        Calculates the Euclidean distance between two points.
        :param other:
        :return Number:
        """
        if len(other) != len(self.pos):
            raise ValueError("The dimensions of the two points do not match.")
        else:
            return sqrt(sum([(self.pos[i] - other[i]) ** 2 for i in range(len(self))]))


class PointWithEuclideanDistance(BasicPoint):
    def __init__(self, pos: MutableSequence, name: Any = None):
        super().__init__(pos, name)


class BasicRoute(AbstractRoute):
    def __init__(self, points: MutableSequence[AbstractPoint], name="BasicRoute"):
        self.points = points
        self.name = name

    def __iter__(self):
        return iter(self.points)

    def __getitem__(self, item):
        return self.points[item]

    def __setitem__(self, item, value):
        self.points[item] = value

    def __delitem__(self, item):
        del self.points[item]

    def __len__(self):
        return len(self.points)

    def __str__(self):
        string = self.name + "(\n"
        for point in self.points:
            string += f"{point.name}: {[point[i] for i in range(len(point))]}\n"
        string += ")"
        return string

    def insert(self, index, value):
        self.points.insert(index, value)

    def distance(self):
        """
        Calculates the total distance.
        :return:
        """
        return sum([pre.distance_to(after) for pre, after in zip(self[:-1], self[1:])])

    def swap(self, index_1: int, index_2: int) -> None:
        """
        Swaps two points
        :param index_1:
        :param index_2:
        :return:
        """
        self[index_1], self[index_2] = self[index_2], self[index_1]

    def append(self, value: AbstractPoint):
        self.points.append(value)


class CircularRoute(BasicRoute):
    def __init__(self, points: MutableSequence[AbstractPoint], name="CircularRoute"):
        super().__init__(points, name)

    def distance(self):
        return super().distance() + self[-1].distance_to(self[0])
