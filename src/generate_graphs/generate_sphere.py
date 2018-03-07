def calculate_radius_sphere(N, A):
    from math import sqrt
    # this is just sqrt(A/N) because I defined my unit sphere on the area 0->1 instead of -1 -> 1
    # I found this a lot easier to work with in terms of buckets/graphing
    return sqrt(A/N)

def generate_random_points(N):
    from random import random
    from math import pi, sqrt, sin, cos
    from .util import distance
    from .node import Node
    results = []
    for n in range(N):
        u = (random() * 2) - 1
        theta = random() * 2 * pi
        x = sqrt(1 - u**2) * cos(theta)
        y = sqrt(1 - u**2) * sin(theta)
        z = u
        node = Node(((x+1)/2, (y+1)/2, (z+1)/2), node_number=n)
        results.append(node)
    return results

def get_adjacent_nodes_for_bucket(x, y, buckets):
	offsets = [(1, -1), (1, 0), (1, 1), (0,1)]
	result = []
	for dx, dy in offsets:
		result = result + buckets[(x+dx) % len(buckets)][(y+dy) % len(buckets)]
	return result

def connect_nodes(nodes, R):
    from .util import distance

    num_buckets = int(1/R) - 1
    num_buckets = 1 if num_buckets <= 0 else num_buckets
    num_buckets = num_buckets
    buckets = []
    for i in range(num_buckets):
        tmp = []
        for _ in range(num_buckets):
            tmp.append([])
        buckets.append(tmp)

    for node in nodes:
        bucket_x = int(node.dims[0]*num_buckets)
        bucket_y = int(node.dims[1]*num_buckets)
        buckets[bucket_x][bucket_y].append(node)
    for x in range(num_buckets):
    	for y in range(num_buckets):
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


def unit_sphere_graph(N, A):
    R = calculate_radius_sphere(N, A)
    nodes = generate_random_points(N)
    nodes = connect_nodes(nodes, R)
    return nodes
