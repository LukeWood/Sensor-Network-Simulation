from coloring import compute_ordering, color_graph
from generate_graphs import unit_square_graph
from generate_graphs import unit_disc_graph
from generate_graphs import unit_sphere_graph
from generate_graphs import adjacency_list_from_node_list

benchmarks = [
    (1,  1000,    32, "square", unit_square_graph),
    (2,  8000,    64, "square", unit_square_graph),
    (3,  16000,   32, "square", unit_square_graph),
    (4,  64000,   64, "square", unit_square_graph),
    (5,  64000,   128,"square", unit_square_graph),
    (6,  128000,  64, "square", unit_square_graph),
    (7,  128000,  128,"square", unit_square_graph),
    (8,  8000,    64, "disc", unit_disc_graph),
    (9,  64000,   64, "disc", unit_disc_graph),
    (10, 64000,   128, "disc", unit_disc_graph),
    (11, 16000,   64, "sphere", unit_sphere_graph),
    (12, 32000,   128,"sphere", unit_sphere_graph),
    (13, 64000,   128,"sphere", unit_sphere_graph)
]

with open("../results/shared/coloring/coloring_data.csv" % topology, "w+") as f:
    f.write("Benchmark,N,A,Topology,Number of Colors Used,Runtime\n")
    for benchmark, N, A, topology, fn in benchmarks:
        print("Running benchmark %d" % benchmark)
