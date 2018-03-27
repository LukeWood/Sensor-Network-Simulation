def distance(n1, n2):
	from math import sqrt
	return sqrt(
		sum(
			[(n1.dims[i] - n2.dims[i])**2 for i in range(len(n1.dims))]
		)
	)

def extract_node_nums(node):
	return list(
		map((lambda node: node.node_number), node.edges)
	)

def adjacency_list_from_node_list(nodes):
	N = len(nodes)
	return list(
		map(extract_node_nums, nodes)
	)

def adjacency_list_to_file(alist, filename=None):
	from json import dumps
	if not filename:
		print(dumps(alist))
	else:
		with open(filename, "w+") as f:
			f.write(dumps(alist))
