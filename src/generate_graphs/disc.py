"""
Generating disc topology
"""

def calculate_radius_disc(N, A):
	from math import sqrt
	from math import pi
	return sqrt(A/(N * pi))

def generate_random_points_disc(N):
	from .node import Node
    from random import random
    from math import sin
    from math import cos
	from math import pi

    result = []
    for n in range(N):
        theta = 2 * pi * rand()
        result.append(Node(cos(theta), sin(theta), node_number=n))
	return result

def node_pairs(node_list):
	from itertools import combinations
	return combinations(node_list, 2)

def unit_disc_graph(N, A):
	from .common import connect_nodes
	R = calculate_radius_disc(N, A)

	nodes = generate_random_points_disc(N)
	nodes = connect_nodes(nodes, R)
	return nodes
