from rgg.coloring import compute_ordering, color_graph, valid_coloring
from rgg.generate_graphs import unit_square_graph
from rgg.generate_graphs import unit_disc_graph
from rgg.generate_graphs import unit_sphere_graph
from rgg.generate_graphs import adjacency_list_from_node_list
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
    f.write("Benchmark,N,A,R,Topology,Avg. Degree,Min Degree,Max Degree,When Removed,Colors,Largest Color,Runtime\n")
    for benchmark, N, A, topology, fn in benchmarks:
        print("Running benchmark %d" % benchmark)
        start = process_time()
        adj_list,R = fn(N, A, return_radius=True)
        ordering, degrees_when_removed = compute_ordering(adj_list)
        coloring = color_graph(ordering, adj_list)
        end = process_time()
        num_colors = max(coloring)
        max_degree_when_removed = max(degrees_when_removed)
        min_degree = min(map(lambda node: len(node),adj_list))
        max_degree = max(map(lambda node: len(node),adj_list))
        avg_degree = sum(map(lambda node: len(node),adj_list))/len(adj_list)
        color_counts = [0 for _ in range(num_colors + 1)]
        for color in coloring:
            color_counts[color] = color_counts[color] + 1
        largest_color = max(color_counts)
        runtime = end - start
        if not valid_coloring(coloring, adj_list):
            raise "OUCH!"
        f.write("%d,%d,%d,%.6f,%s,%d,%d,%d,%d,%d,%d,%.6f" % (benchmark, N, A, R, topology,avg_degree,min_degree,max_degree, max_degree_when_removed, num_colors,largest_color, runtime))
        f.write("\n")
        f.flush()
