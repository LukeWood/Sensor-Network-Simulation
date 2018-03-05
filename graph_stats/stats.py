from functools import reduce

def total_edges(nodes):
	degrees = map((lambda x: len(x.edges)), nodes)
	return reduce((lambda acc, x: acc + x), degrees)

def average_degree(nodes):
    N = len(nodes)
    return total_edges(nodes)/N
	
def max_degree(nodes):
	degrees = map((lambda x: len(x.edges)), nodes)
	return reduce((lambda acc, x: x if x > acc else acc), degrees)

def min_degrees(nodes):
    degrees = map((lambda x: len(x.edges)), nodes)
    return reduce((lambda acc, x: x if x < acc else acc), degrees)
