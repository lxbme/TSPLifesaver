# TSP Lifesaver
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com) 

**!!! This package is currently under development and may contain bugs. !!!**

## Introduction

This is a framework that simplifies the process of solving TSP (Traveling Salesman Problem) problems.

## Installation 

```python
pip install TSPLifesaver
```

## Quick Start

### How to import:
```python
from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance
from TSPLifesaver.optimizer import SimulatedAnnealing
from TSPLifesaver.tools import route_from_sequence, simulated_annealing
```

### Define a point:
```python
point = PointWithEuclideanDistance([1,1,1], name="test_point")
print(point)
# test_point([1,1,1])

print(point.distance_to(point))
# 0

print(point.distance_to([1,1,2]))
# 1
```

### Define a route:
```python
points = [PointWithEuclideanDistance(i) for i in [[1,1,1],[2,2,2],[3,3,3]]]
route = BasicRoute(points, name="TestRoute")

#or you can
route = route_from_sequence([[1,1,1],[2,2,2],[3,3,3]])

print(route)

# TestRoute(
# None: [1, 1, 1]
# None: [2, 2, 2]
# None: [3, 3, 3]
# )
```

### Calculate total distance:
```python
print(route.distance())
# 6.928203230275509
```

### **Optimize the route:**
```python
optimizer = SimulatedAnnealing(route, temperature=10000, cooling_rate=0.003, min_temperature=1)
route = optimizer.optimize()

# or you can 
optimized_route = simulated_annealing(route,epoch=50)
```
