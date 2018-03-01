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

import math

import itertools

import random
from random import random as rand

from functools import reduce

class Node():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.edges = []

def distance(n1, n2):
	dx = abs(n1.x - n2.x)
	dy = abs(n1.y - n2.y)
	return math.sqrt(dx*dx + dy*dy)

def unit_square_graph(N, A, seed=None):
	if seed:
		random.seed(seed)

	nodes = []
	for _ in range(N):
		nodes.append(Node(rand(), rand()))

	R = math.sqrt(A/(N * math.pi))

	for n1, n2 in itertools.product(nodes, repeat=2):
		if distance(n1, n2) < R:
			n1.edges.append(n2)
			n2.edges.append(n1)
	degrees = map((lambda x: len(x.edges)), nodes)
	average_degree = reduce((lambda x, y: x + y/N), degrees)
	print(average_degree)
graph = unit_square_graph(100,  2)
