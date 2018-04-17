def get_adjacent_nodes_for_bucket(x, y, buckets):
	offsets = [(1, -1), (1, 0), (1, 1), (0,1)]
	result = []
	for dx, dy in offsets:
		result = result + buckets[(x+dx) % len(buckets)][(y+dy) % len(buckets)]
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
					if n1 == n2:
						continue
					if distance(n1, n2) <= R:
						n1.edges.append(n2.node_number)
						n2.edges.append(n1.node_number)
			for n1 in base_nodes:
				for n2 in base_nodes:
					if n1 == n2:
						continue
					if distance(n1, n2) <= R:
						n1.edges.append(n2.node_number)
	return list(map((lambda node: list(set(node.edges))), nodes))

def generate_graph(N, A, radius_function, point_generation_function, return_positions=False, return_radius=False):
	R = radius_function(N, A)
	nodes = point_generation_function(N)
	if return_positions and return_radius:
		dims = list(map((lambda node: node.dims), nodes))
		return connect_nodes(nodes, R), dims, R
	if return_positions:
		dims = list(map((lambda node: node.dims), nodes))
		return connect_nodes(nodes, R), dims
	elif return_radius:
		return connect_nodes(nodes, R), R
	return connect_nodes(nodes, R)
