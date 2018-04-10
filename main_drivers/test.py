from rgg.coloring import color_graph, compute_ordering
from rgg.generate_graphs import unit_square_graph
from rgg.generate_graphs import adjacency_list_from_node_list
from time import process_time

benchmarks = [
    (2000, 32)
]

for N, A in benchmarks:
    adj_list = unit_square_graph(N, A)
    ordering, _ = compute_ordering(adj_list)
    coloring = color_graph(ordering, adj_list)
    print(max(coloring))
