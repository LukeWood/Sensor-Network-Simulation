from coloring import color_graph, compute_ordering
from generate_graphs import unit_square_graph
from generate_graphs import adjacency_list_from_node_list
from time import process_time

benchmarks = [
    (8000, 64)
]

for N, A in benchmarks:
    nodes = unit_square_graph(N, A)
    adj_list = adjacency_list_from_node_list(nodes)

    ordering = compute_ordering(adj_list)
    coloring = color_graph(ordering, adj_list)
    print(max(coloring))
