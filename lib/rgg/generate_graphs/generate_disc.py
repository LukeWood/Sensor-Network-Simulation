"""
Generating disc topology
"""

def calculate_radius_disc(N, A):
	from math import sqrt
	from math import pi
	return sqrt(A/N)/2

def generate_random_points(N):
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

def unit_disc_graph(N, A, **kwargs):
	from .common import generate_graph
	return generate_graph(N, A, calculate_radius_disc, generate_random_points, **kwargs)
