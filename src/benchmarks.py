from coloring import compute_ordering, color_graph
from generate_graphs import unit_square_graph
from generate_graphs import unit_disc_graph
from generate_graphs import unit_sphere_graph
from generate_graphs import adjacency_list_from_node_list
from time import process_time

benchmarks = [
    (1,  1000,    32, "Square", unit_square_graph),
    (2,  8000,    64, "Square", unit_square_graph),
    (3,  16000,   32, "Square", unit_square_graph),
    (4,  64000,   64, "Square", unit_square_graph),
    (5,  64000,   128,"Square", unit_square_graph),
    (6,  128000,  64, "Square", unit_square_graph),
    (7,  128000,  128,"Square", unit_square_graph),
    (8,  8000,    64, "Disc",   unit_disc_graph),
    (9,  64000,   64, "Disc",   unit_disc_graph),
    (10, 64000,   128,"Disc",   unit_disc_graph),
    (11, 16000,   64, "Sphere", unit_sphere_graph),
    (12, 32000,   128,"Sphere", unit_sphere_graph),
    (13, 64000,   128,"Sphere", unit_sphere_graph)
]

with open("../results/shared/coloring/coloring_data.csv", "w+") as f:
    f.write("Benchmark,N,A,Topology,Number of Colors Used,Runtime\n")
    for benchmark, N, A, topology, fn in benchmarks:
        print("Running benchmark %d" % benchmark)
        start = process_time()
        nodes = fn(N, A)
        adj_list = adjacency_list_from_node_list(nodes)
        ordering = compute_ordering(adj_list)
        coloring = color_graph(ordering, adj_list)
        end = process_time()
        colors = max(coloring)
        runtime = end - start
        f.write("%d,%d,%d,%s,%d,%.6f" % (benchmark, N, A, topology, colors, runtime))
        f.write("\n")
        f.flush()
