import random
import math
from copy import deepcopy

from TSPLifesaver.abc import AbstractRoute, AbstractPoint
from TSPLifesaver.abc.abc import AbstractOptimizer


class SimulatedAnnealing(AbstractOptimizer):
    def __init__(self, initial_route: AbstractRoute, temperature, cooling_rate, min_temperature):
        """
        :param initial_route:
        :param initial_route:
        :param temperature:
        :param cooling_rate:
        :param min_temperature:
        """
        self.current_route = deepcopy(initial_route)
        self.best_route = deepcopy(initial_route)
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature

    def optimize(self):
        while self.temperature > self.min_temperature:
            new_route = deepcopy(self.current_route)

            # exchange randomly
            i, j = random.sample(range(len(new_route)), 2)
            new_route.swap(i, j)

            # calc cost
            current_cost = self.current_route.distance()
            new_cost = new_route.distance()
            cost_difference = current_cost - new_cost

            # accepting the new result?
            if cost_difference > 0 or math.exp(cost_difference / self.temperature) > random.random():
                self.current_route = new_route
                if new_cost < self.best_route.distance():
                    self.best_route = new_route

            # decrease the temperature
            self.temperature *= (1 - self.cooling_rate)

        return self.best_route


class ExhaustiveIndexing(AbstractOptimizer):
    def __init__(self, initial_route: AbstractRoute, max_iterations: int = None):
        self.best_route = deepcopy(initial_route)
        self.max_iterations = max_iterations
        self.count = 0

    def _permute(self, route: AbstractRoute, current_index=0):
        if current_index == len(route):
            yield route

        else:
            for i in range(current_index, len(route)):
                route.swap(current_index, i)
                yield from self._permute(route, current_index + 1)
                route.swap(current_index, i)

    def optimize(self):
        for route in self._permute(deepcopy(self.best_route)):
            # print("length of current route: ", route.length())
            if self.max_iterations is not None and self.count >= self.max_iterations:
                break

            if route.distance() < self.best_route.distance():
                self.best_route = deepcopy(route)
            self.count += 1

        return self.best_route
