def calculate_radius_sphere(N, A):
    from math import sqrt
    from math import pi
    return sqrt(A/N)*2

def generate_random_points(N):
    from numpy.random import uniform
    from .node import Node
    xs = uniform(0, 1, N)
    ys = uniform(0, 1, N)
    return [Node(xs[i], ys[i], node_number=i) for i in range(N)]

def node_pairs(node_list):
    from itertools import combinations
    return combinations(node_list, 2)

def get_adjacent_nodes_for_bucket(x, y, buckets):
    offsets = [(1, -1), (1, 0), (1, 1), (0,1)]
    result = []
    for dx, dy in offsets:
        if x + dx >= len(buckets):
            continue
        if y + dy >= len(buckets):
            continue
        result = result + buckets[x+dx][y+dy]
    return result

def unit_sphere_graph(N, A):
    from .common import connect_nodes
    R = calculate_radius_sphere(N, A)
    nodes = generate_random_points(N)
    nodes = connect_nodes(nodes, R)
    return nodes
