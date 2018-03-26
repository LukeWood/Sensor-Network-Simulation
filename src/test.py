from coloring import color_graph
from generate_graphs import unit_square_graph
from generate_graphs import adjacency_list_from_node_list
N=10000
A=64
nodes = unit_square_graph(N, A)
adj_list = adjacency_list_from_node_list(nodes)

min_colors = color_graph(adj_list)
print(min_colors)
