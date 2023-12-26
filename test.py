from TSPLifesaver.structure import BasicRoute, PointWithEuclideanDistance

print(PointWithEuclideanDistance([1,2],name="test"))
points = [PointWithEuclideanDistance(i,) for i in [[1,1,1],[2,2,2],[3,3,3]]]
route = BasicRoute(points, name="TestRoute")
print(route.distance())