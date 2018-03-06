def distance2D(n1, n2):
	from math import sqrt
	dx = (n1.x - n2.x)
	dy = (n1.y - n2.y)
	return sqrt((dx*dx) + (dy*dy))

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
