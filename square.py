def plot_edge_densities_square(N, A, output_dir=""):
    from generate_graphs import unit_square_graph
    adjacency_list, nodes = unit_square_graph(N, A)
    from stats import max_degree
    from charts import edge_density_histogram
    degrees = list(map((lambda x: x.count(1)),adjacency_list))
    edge_density_histogram(degrees, max_degree(nodes), graph_shape="Square", name="%s%d_%d.png" % (output_dir, N, A))

def plot_runtime_chart(N, A, output_dir=""):
    from generate_graphs import unit_square_graph


Ns = [
    1000, 2000, 5000, 10000
]
As = [
    5, 10, 25, 50, 100, 200
]

for N in Ns:
    for A in As:
        plot_edge_densities_square(N, A, output_dir="outputs/square/")
        plot_runtime_chart(N, A, output_dir="outputs/square/")
