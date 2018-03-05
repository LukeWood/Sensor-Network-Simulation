import random
import time
random.seed(time.time())

def plot_edge_densities_square(N, A, output_dir=""):
    from generate_graphs import unit_square_graph
    nodes = unit_square_graph(N, A)
    from graph_stats import max_degree
    from charts import edge_density_histogram
    degrees = list(map((lambda x: len(x.edges)), nodes))
    edge_density_histogram(degrees, max_degree(nodes), graph_topology="Square", name="%s%d_%d.png" % (output_dir, N, A))

def time_run(N, A):
    from time import process_time
    from generate_graphs import unit_square_graph
    start = process_time()
    nodes = unit_square_graph(N, A)
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
    runtime_chart(Ns, runtimes, graph_topology="Square", name="%sruntime_chart.png" % output_dir, expected_order=1)
    print("\nDone Creating Runtime Chart")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate the charts for square sensor network topology")
    parser.add_argument("--runtimes",     dest='runtimes',     action='store_true')
    parser.add_argument("--edge_density", dest='edge_density', action='store_true')
    parser.add_argument("--test",         dest='test',         action='store_true')
    parser.set_defaults(runtimes=False, edge_density=False, test=False)
    args = parser.parse_args()

    A = 64

    if args.edge_density:
        print("Creating Edge Density Chart")
        N = 8000
        plot_edge_densities_square(N, A, output_dir="outputs/square/edge_density/")

    if args.runtimes:
        Ns = [10, 20, 50, 100, 500, 1000, 2000, 2500, 3000, 4000, 5000, 7500, 10000, 12000, 20000, 30000, 50000, 100000]
        plot_runtime_chart(Ns, A,  output_dir="outputs/square/runtime/")

    if args.test:
        from generate_graphs import unit_square_graph
        from generate_graphs import calculate_radius_square

        N = 20000
        nodes = unit_square_graph(N, A)

        from graph_stats import total_edges, average_degree, max_degree, min_degree

        print("\n=== TEST RESULTS ===")
        print("Graph Size:              %d" % N)
        print("Expected Average Degree: %d" % A)
        print("R:                       %f" % calculate_radius_square(N, A))
        print("Average Degree:          %f" % average_degree(nodes))
        print("Max Degree:              %f" % max_degree(nodes))
        print("Min Degree:              %f" % min_degree(nodes))
        print("=== TEST ENDING ===\n")
