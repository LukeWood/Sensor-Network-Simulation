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
	from .util import random_node
	return [random_node(node_number) for node_number in range(N)]

def node_pairs(node_list):
	from itertools import combinations
	return combinations(node_list, 2)

def get_nodes_for_bucket(x, y, buckets):
	offsets = [-1, 0, 1]
	result = []
	for dx in offsets:
		for dy in offsets:
			if x + dx < 0:
				continue
			if y + dy < 0:
				continue
			if x + dx >= len(buckets):
				continue
			if y + dy >= len(buckets):
				continue
			result = result + buckets[x+dx][y+dy]
	return result

def connect_nodes(nodes, R):
	from math import ceil
	from .util import distance2D

	num_buckets_p = ceil(1/R) + 1
	buckets = []
	for _ in range(num_buckets_p+1):
		buckets.append([[] for _ in range(num_buckets_p+1)])

	for node in nodes:
		bucket_num_x = int(node.x * num_buckets_p)
		bucket_num_y = int(node.y * num_buckets_p)
		buckets[bucket_num_x][bucket_num_y].append(node)

	for x in range(num_buckets_p):
		for y in range(num_buckets_p):
			base_nodes = buckets[x][y]
			operation_nodes = get_nodes_for_bucket(x, y, buckets)
			for n1 in base_nodes:
				for n2 in operation_nodes:
					if distance2D(n1, n2) <= R:
						n1.edges.append(n2)
	return nodes

def unit_square_graph(N, A):
	R = calculate_radius_square(N, A)
	nodes = generate_random_points(N)
	nodes = connect_nodes(nodes, R)

	from .util import adjacency_list_from_node_list
	adjacency_list = adjacency_list_from_node_list(nodes)

	return adjacency_list, nodes
