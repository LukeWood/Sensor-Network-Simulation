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

def connect_nodes(nodes, R):
	from math import floor
	from .util import distance2D

	num_buckets_p = int(1/R) - 1
	num_buckets_p = 1 if num_buckets_p < 1 else num_buckets_p
	buckets = []
	for _ in range(num_buckets_p):
		buckets.append([[] for _ in range(num_buckets_p)])

	for node in nodes:
		bucket_num_x = int(node.x * num_buckets_p)
		bucket_num_y = int(node.y * num_buckets_p)
		buckets[bucket_num_x][bucket_num_y].append(node)

	for x in range(num_buckets_p):
		for y in range(num_buckets_p):
			base_nodes = buckets[x][y]
			operation_nodes = get_adjacent_nodes_for_bucket(x, y, buckets)
			for n1 in base_nodes:
				for n2 in operation_nodes:
					if distance2D(n1, n2) <= R:
						n1.edges.append(n2)
						n2.edges.append(n1)
			for n1 in base_nodes:
				for n2 in base_nodes:
					#TODO(lukewood) do these nodes connect to themselves?
					#is this desired behavior
					if distance2D(n1, n2) <= R:
						n1.edges.append(n2)
	return nodes

def unit_square_graph(N, A):
	R = calculate_radius_square(N, A)

	nodes = generate_random_points(N)
	nodes = connect_nodes(nodes, R)

	return nodes
