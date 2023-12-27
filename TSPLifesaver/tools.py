from typing import Iterable, MutableSequence, Type

from TSPLifesaver.abc import AbstractRoute, AbstractPoint
from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance


def route_from_sequence(sequence: Iterable[MutableSequence], route: AbstractRoute = BasicRoute([]),
                        point_class: Type[AbstractPoint] = PointWithEuclideanDistance,
                        name_offset: int = 1,) -> AbstractRoute:
    """
    :param route: Instances of the AbstractRoute class or its subclasses, defaults to empty instance of BasicRoute
    :param name_offset: Index of the name
    :param sequence: Sequence containing coordinates
    :param point_class: AbstractPoint or its subclasses ,defaults to PointWithEuclideanDistance
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


if __name__ == "__main__":
    print(route_from_sequence([[1,1],[2,2]]))
