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
	from math import pi, sqrt, sin, cos
	result = []
	for n in range(N):
		r = random()
		theta = 2*pi*random()
		x = sqrt(r) * cos(theta)
		y = sqrt(r) * sin(theta)
		x = x/2 + 0.5
		y = y/2 + 0.5
		node = Node((x, y), node_number=n)
		result.append(node)
	return result

def unit_disc_graph(N, A, **kwargs):
	from .common import generate_graph
	return generate_graph(N, A, calculate_radius_disc, generate_random_points, **kwargs)
