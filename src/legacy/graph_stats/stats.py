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

def min_degree(nodes):
	degrees = map((lambda x: len(x.edges)), nodes)
	return reduce((lambda acc, x: x if x < acc else acc), degrees)

def gather_statistics(Ns, A, implementation, output_dir=""):
	from time import process_time

	with open(output_dir + "data.csv", "w+") as f:
		f.write("Nodes,E(Avg. Deg),Avg. Deg,Max Deg.,Min Deg.,Seconds\n")
		for N in Ns:
			print("Timing %d" % N)
			start = process_time()
			nodes = implementation(N, A)
			end = process_time()
			runtime = end - start
			f.write("%d,%d,%f,%d,%d,%f\n" % (N, A, average_degree(nodes), max_degree(nodes), min_degree(nodes), runtime))
