"""
Generating disc topology
"""

def calculate_radius_disc(N, A):
	from math import sqrt
	from math import pi
	return sqrt(A/N)/2

def generate_random_points_disc(N):
	from .node import Node
	from .util import distance
	from random import random
	center_node = Node((.5, .5))
	result = []
	n = 0;
	while n < N:
		x = random()
		y = random()
		node = Node((x, y), node_number=n)
		if distance(node, center_node) <= .5:
			result.append(node)
			n = n + 1
	return result

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
	from .util import distance
	from math import pi

	num_buckets_p = int(1/R) - 1
	num_buckets_p = 1 if num_buckets_p < 1 else num_buckets_p
	buckets = []
	for _ in range(num_buckets_p):
		buckets.append([[] for _ in range(num_buckets_p)])

	for node in nodes:
		bucket_num_x = int((1+(node.dims[0]))/2 * num_buckets_p)
		bucket_num_y = int((1+(node.dims[1]))/2 * num_buckets_p)
		buckets[bucket_num_x][bucket_num_y].append(node)

	for x in range(num_buckets_p):
		for y in range(num_buckets_p):
			base_nodes = buckets[x][y]
			operation_nodes = get_adjacent_nodes_for_bucket(x, y, buckets)
			for n1 in base_nodes:
				for n2 in operation_nodes:
					if distance(n1, n2) <= R:
						n1.edges.append(n2)
						n2.edges.append(n1)
			for n1 in base_nodes:
				for n2 in base_nodes:
					if n1 == n2:
						continue
					if distance(n1, n2) <= R:
						n1.edges.append(n2)
	return nodes

def node_pairs(node_list):
	from itertools import combinations
	return combinations(node_list, 2)

def unit_disc_graph(N, A):
	R = calculate_radius_disc(N, A)
	nodes = generate_random_points_disc(N)
	nodes = connect_nodes(nodes, R)
	return nodes