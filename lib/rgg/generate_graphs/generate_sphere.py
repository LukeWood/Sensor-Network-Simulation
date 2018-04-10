def calculate_radius_sphere(N, A):
    from math import sqrt
    # this is just sqrt(A/N) because I defined my unit sphere on the area 0->1 instead of -1 -> 1
    # I found this a lot easier to work with in terms of buckets/graphing
    return sqrt(A/N)

def generate_random_points(N):
    from random import random
    from math import pi, sqrt, sin, cos
    from .util import distance
    from .node import Node
    results = []
    for n in range(N):
        u = (random() * 2) - 1
        theta = random() * 2 * pi
        x = sqrt(1 - u**2) * cos(theta)
        y = sqrt(1 - u**2) * sin(theta)
        z = u
        node = Node(((x+1)/2, (y+1)/2, (z+1)/2), node_number=n)
        results.append(node)
    return results


def unit_sphere_graph(N, A):
    from .common import generate_graph
    return generate_graph(N, A, calculate_radius_sphere, generate_random_points)
