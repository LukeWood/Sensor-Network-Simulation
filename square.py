def plot_edge_densities_square(N, A, output_dir=""):
    from generate_graphs import unit_square_graph
    adjacency_list, nodes = unit_square_graph(N, A)
    from stats import max_degree
    from charts import edge_density_histogram
    degrees = list(map((lambda x: x.count(1)),adjacency_list))
    edge_density_histogram(degrees, max_degree(nodes), graph_topology="Square", name="%s%d_%d.png" % (output_dir, N, A))

def time_run(N, A):
    from time import process_time
    from generate_graphs import unit_square_graph
    start = process_time()
    adjacency_list, nodes = unit_square_graph(N, A)
    end =   process_time()
    return end - start

def plot_runtime_chart(Ns, A, output_dir=""):
    from generate_graphs import unit_square_graph
    from charts import runtime_chart

    runtimes = [time_run(N, A) for N in Ns]
    runtime_chart(Ns, runtimes, graph_topology="Square", name=output_dir)

Ns = [
    1000, 2000, 3000, 4000
]
As = [
    5, 10, 25, 50, 100, 200
]

#for N in Ns:
#    for A in As:
#        plot_edge_densities_square(N, A, output_dir="outputs/square/")

plot_runtime_chart(Ns, 10)
