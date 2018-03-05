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

    print("Creating Runtime Chart")
    runtimes = []
    for i, N in enumerate(Ns):
        from sys import stdout
        print("Generating Graph of Size %d Nodes. Item %d/%d" % (N, i+1, len(Ns)))
        stdout.write("\033[F")
        runtimes.append(time_run(N, A))
    runtime_chart(Ns, runtimes, graph_topology="Square", name="%sruntime_chart.png" % output_dir)
    print("\nDone Creating Runtime Chart")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate the charts for square sensor network topology")
    parser.add_argument("--runtimes",     dest='runtimes',     action='store_true')
    parser.add_argument("--edge_density", dest='edge_density', action='store_true')
    parser.set_defaults(runtimes=False, edge_density=False)
    args = parser.parse_args()

    Ns = [10, 20, 50, 100, 500, 1000, 2000, 2500, 3000, 4000, 5000, 7500, 10000, 12000 ]
    A = 50

    if args.edge_density:
        print("Creating Edge Density Chart")
        for N in Ns:
            plot_edge_densities_square(N, A, output_dir="outputs/square/edge_density/")

    if args.runtimes:
        plot_runtime_chart(Ns, A,  output_dir="outputs/square/runtime/")
