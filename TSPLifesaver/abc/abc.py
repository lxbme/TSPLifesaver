from collections.abc import MutableSequence
from abc import ABC, abstractmethod
from numbers import Number


class AbstractPoint(ABC, MutableSequence):
    def __delitem__(self, key): ...

    def insert(self, index, value): ...

    @abstractmethod
    def __init__(self,pos):
        """
        Init the Point
        :param pos:
        """

    @property
    def name(self):
        """
        The name of the Point.
        :return: Any
        """
        return None

    @abstractmethod
    def distance_to(self, other: MutableSequence):
        """
        Calculate the distance between this Point and another.
        :param other:
        :return The distance between the:
        """


class AbstractRoute(ABC, MutableSequence):
    @abstractmethod
    def swap(self, index_1: int, index_2: int) -> None:
        """
        This method should swap the positions of the two elements by indexes.
        """

    @abstractmethod
    def distance(self):
        """
        This method should return the total length of the route.
        :return Number: The total length of the route:
        """


class AbstractOptimizer(ABC):
    @abstractmethod
    def optimize(self):
        """
        This method should start the process of optimization and return the result.
        """
