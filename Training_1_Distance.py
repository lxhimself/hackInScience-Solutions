import math

points = [1, 4, 2, 8, 1652]

def dist(points):
    points.sort()
    A = [points[0]]
    B = [points[-1]]
    print(math.dist(A, B))


dist(points)


