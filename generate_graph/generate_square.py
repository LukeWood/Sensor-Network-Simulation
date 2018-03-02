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

def generate_random_points(N, A):
	from util import random_node
	return [random_node() for _ in range(N)]

def node_pairs(list):
	from itertools import combinations
	return combinations(list, 2)

def unit_square_graph(N, A):
	R = calculate_radius_square(N, A)
	nodes = generate_random_points(N, A)

	for n1, n2 in node_pairs(nodes):
		from util import distance2D
		if distance2D(n1, n2) <= R:
			n1.edges.append(n2)
			n2.edges.append(n1)

	from util import graph_stats
	total_edges, average_degree, max_degree, min_degree = graph_stats(nodes)

	from util import adjacency_list_from_node_list
	adjacency_list = adjacency_list_from_node_list(nodes)

	return adjacency_list, R, total_edges, average_degree, max_degree, min_degree

if __name__ == "__main__":
	adjacency_list, R, total_edges, average_degree, max_degree, min_degree = unit_square_graph(1000,  2.5)

	print("Radius:         %f" % R)
	print("Total edges:    %f" % total_edges)
	print("Average Degree: %f" % average_degree)
	print("Max Degree:     %f" % max_degree)
	print("Min Degree:     %f" % min_degree)
