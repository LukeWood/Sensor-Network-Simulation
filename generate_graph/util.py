def random_node(node_number=None):
	from node import Node
	from random import random
	return Node(random(), random(), node_number=node_number)

def distance2D(n1, n2):
	from math import sqrt
	dx = abs(n1.x - n2.x)
	dy = abs(n1.y - n2.y)
	return sqrt(dx*dx + dy*dy)

def graph_stats(nodes):
	from functools import reduce
	N = len(nodes)
	degrees 	   = list(map((lambda x: len(x.edges)), 			nodes))
	total_edges    = reduce((lambda acc, x: acc + x), 				degrees)
	max_degree 	   = reduce((lambda acc, x: x if x > acc else acc), degrees)
	min_degree 	   = reduce((lambda acc, x: x if x < acc else acc), degrees)
	average_degree = total_edges/N
	return total_edges, average_degree, max_degree, min_degree

def row_from_node(node, N):
	edges = [0 for x in range(N)]
	for connected_node in node.edges:
		edges[connected_node.node_number] = 1
	return edges

def adjacency_list_from_node_list(nodes):
	N = len(nodes)
	return list(
		map((lambda node: row_from_node(node, N)), nodes)
	)
