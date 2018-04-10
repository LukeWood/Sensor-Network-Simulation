"""
File Doc:

N = number of sensors (vertices)
A = expected density (average degree) of the sensor network
T = network topology (unit square, unit disk, or unit sphere)

r = estimated radius r value
E = number of distinct pairwise sensor adjacencies (edges)
"""

def calculate_radius_square(N, A):
    from math import sqrt
    from math import pi
    return sqrt(A/(N * pi))

def generate_random_points(N):
    from numpy.random import uniform
    from .node import Node
    xs = uniform(0, 1, N)
    ys = uniform(0, 1, N)
    return [Node((xs[i], ys[i]), node_number=i) for i in range(N)]

def unit_square_graph(N, A, return_positions=False):
    from .common import generate_graph
    return generate_graph(N, A, calculate_radius_square, generate_random_points, return_positions=return_positions)
