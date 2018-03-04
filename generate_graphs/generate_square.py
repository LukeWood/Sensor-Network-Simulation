"""
File Doc:

N = number of sensors (vertices)
A = expected density (average degree) of the sensor network
T = network topology (unit square, unit disk, or unit sphere)

r = estimated radius r value
E = number of distinct pairwise sensor adjacencies (edges)
Avg. Deg. = real density (average degree) of the generated sensor network
Max  Deg. = max degree of sensor networks (RGG's)
Min  deg. = minimum degree of the generated networks (RGG's)
"""

def calculate_radius_square(N, A):
	from math import sqrt
	from math import pi
	return sqrt(A/(N * pi))

def generate_random_points(N):
	from .util import random_node
	return [random_node(node_number) for node_number in range(N)]

def node_pairs(node_list):
	from itertools import combinations
	return combinations(node_list, 2)

def unit_square_graph(N, A):
	R = calculate_radius_square(N, A)
	nodes = generate_random_points(N)

	for n1, n2 in node_pairs(nodes):
		from .util import distance2D
		if distance2D(n1, n2) <= R:
			n1.edges.append(n2)
			n2.edges.append(n1)

	from .util import adjacency_list_from_node_list
	adjacency_list = adjacency_list_from_node_list(nodes)

	return adjacency_list, nodes
