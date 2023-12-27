from typing import Iterable, MutableSequence, Type
from random import shuffle
from copy import deepcopy

from TSPLifesaver.abc import AbstractRoute, AbstractPoint
from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance
from TSPLifesaver.optimizer import SimulatedAnnealing


def route_from_sequence(sequence: Iterable[MutableSequence], route: AbstractRoute = BasicRoute([]),
                        point_class: Type[AbstractPoint] = PointWithEuclideanDistance,
                        name_offset: int = 1, ) -> AbstractRoute:
    """
    :param route: Instances of the AbstractRoute class or its subclasses, defaults to empty instance of BasicRoute
    :param name_offset: Index of the name
    :param sequence: Sequence containing coordinates
    :param point_class: AbstractPoint or its subclasses ,defaults to PointWithEuclideanDistance
    :return: a new route
    """
    index = name_offset

    for pos in sequence:
        try:
            point = point_class(pos, name=f"{index}")
        except:
            point = point_class(pos)

        route.append(point)
        index += 1

    return route


def simulated_annealing(route: AbstractRoute, epoch: int = 100, temperature: float = 10000,
                        cooling_rate: float = 0.03, min_temperature: float = 1,
                        log: bool = False) -> AbstractRoute:
    """
    :param route: Instances of the AbstractRoute class or its subclasses
    :param epoch: Number of epochs to simulate, defaults to 100
    :param temperature: Temperature of the annealing, defaults to 10000
    :param cooling_rate: Cooling rate of the annealing, defaults to 0.03
    :param min_temperature: Minimum temperature of the annealing, defaults to 1
    :param log: Whether to print the log of the annealing, defaults to False
    :return: optimized route
    """
    if len(route):
        best_route = deepcopy(route)
        for i in range(epoch):
            if log:
                print(f"Running epoch {i} of {epoch}")
            shuffle(route)
            opt = SimulatedAnnealing(route, temperature=temperature,
                                     cooling_rate=cooling_rate, min_temperature=min_temperature)
            current_route = opt.optimize()
            if current_route.distance() < best_route.distance():
                best_route = deepcopy(current_route)
        return best_route
    else:
        return route


if __name__ == "__main__":
    print(simulated_annealing(route_from_sequence([[1, 1], [0, 0], [1, 0], [0, 1]]),log=True))
