def calculate_radius_sphere(N, A):
    from math import sqrt
    from math import pi
    return sqrt(A/N)/4

def generate_random_points(N):
    from random import random
    from .util import distance
    from .node import Node
    n = 0
    root_node = Node((.5, .5, .5))
    results = []
    while n < N:
        node = Node([random(), random(), random()], node_number=n)
        if distance(node, root_node) < .5:
            results.append(node)
            n = n + 1
    return results

def connect_nodes(nodes, R):
    num_buckets = int(1/R) - 1
    num_buckets = 1 if num_buckets <= 0 else num_buckets

    buckets = []
    for i in range(num_buckets):
        tmp = []
        for _ in range(num_buckets):
            tmp.append([])
        buckets.append(tmp)

    for node in nodes:
        buckets[int(node.dims[0]*num_buckets)][int(node.dims[1]*num_buckets)].append(node)



def unit_sphere_graph(N, A):
    R = calculate_radius_sphere(N, A)
    nodes = generate_random_points(N)
    nodes = connect_nodes(nodes, R)
    return nodes
