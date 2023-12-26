# TSP Lifesaver
**!!! This package is currently under development and may contain bugs. !!!**

## Introduction

This is a toolset that simplifies the process of solving TSP (Traveling Salesman Problem) problems.

## Usage

How to import:
```python
from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance
from TSPLifesaver.optimizer import SimulatedAnnealing
from TSPLifesaver.tools import #still_developing
```

Define a point:
```python
point = PointWithEuclideanDistance([1,1,1], name="test_point")
print(point)
# test_point([1,1,1])

print(point.distance_to(point))
# 0

print(point.distance_to([1,1,2]))
# 1
```

Define a route:
```python
points = [PointWithEuclideanDistance(i) for i in [[1,1,1],[2,2,2],[3,3,3]]]
route = BasicRoute(points, name="TestRoute")
print(route)

# TestRoute(
# None: [1, 1, 1]
# None: [2, 2, 2]
# None: [3, 3, 3]
# )
```

Calculate total distance:
```python
print(route.distance())
# 6.928203230275509
```

**Optimize the route:**
```python
optimizer = SimulatedAnnealing(route, temperature=10000, cooling_rate=0.003, min_temperature=1)
route = optimizer.optimize()
```
