import random
import time
random.seed(time.time())

def plot_edge_densities_disc(N, A, output_dir=""):
    from generate_graphs import unit_disc_graph
    nodes = unit_disc_graph(N, A)
    from graph_stats import max_degree
    from charts import edge_density_histogram
    degrees = list(map((lambda x: len(x.edges)), nodes))
    edge_density_histogram(degrees, max_degree(nodes), graph_topology="Disc", name="%s%d_%d.png" % (output_dir, N, A))

def time_run(N, A):
    from time import process_time
    from generate_graphs import unit_disc_graph
    start = process_time()
    nodes = unit_disc_graph(N, A)
    end =   process_time()
    return end - start

def plot_runtime_chart(Ns, A, output_dir=""):
    from generate_graphs import unit_disc_graph
    from charts import runtime_chart

    print("Creating Runtime Chart")
    runtimes = []
    for i, N in enumerate(Ns):
        from sys import stdout
        print("Generating Graph of Size %d Nodes. Item %d/%d" % (N, i+1, len(Ns)))
        stdout.write("\033[F")
        runtimes.append(time_run(N, A))
    runtime_chart(Ns, runtimes, graph_topology="disc", name="%sruntime_chart.png" % output_dir, expected_order=1)
    print("\nDone Creating Runtime Chart")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate the charts for disc sensor network topology")
    parser.add_argument("--runtimes",     dest='runtimes',     action='store_true')
    parser.add_argument("--edge_density", dest='edge_density', action='store_true')
    parser.add_argument("--test",         dest='test',         action='store_true')
    parser.add_argument("--benchmarks",   dest='benchmarks',   action='store_true')
    parser.add_argument("--draw",   dest='draw',   action='store_true')

    parser.set_defaults(runtimes=False, edge_density=False, test=False, benchmarks=False, draw=False)
    args = parser.parse_args()

    A = 64

    if args.edge_density:
        print("Creating Edge Density Chart")
        N = 8000
        plot_edge_densities_disc(N, A, output_dir="../results/disc/edge_density/")

    if args.runtimes:
        Ns = [1000, 4000, 8000, 16000, 32000]
        plot_runtime_chart(Ns, A,  output_dir="../results/disc/runtime/")

    if args.benchmarks:
        from graph_stats import gather_statistics
        from generate_graphs import unit_disc_graph
        Ns = [1000, 5000, 25000, 50000, 100000]
        gather_statistics(Ns, A, unit_disc_graph, output_dir="../results/disc/benchmarks/")

    if args.test:
        from generate_graphs import unit_disc_graph
        from generate_graphs import calculate_radius_disc

        N = 15000
        nodes = unit_disc_graph(N, A)

        from graph_stats import total_edges, average_degree, max_degree, min_degree

        print("\n=== TEST RESULTS ===")
        print("Graph Size:              %d" % N)
        print("Expected Average Degree: %d" % A)
        print("R:                       %f" % calculate_radius_disc(N, A))
        print("Average Degree:          %f" % average_degree(nodes))
        print("Max Degree:              %f" % max_degree(nodes))
        print("Min Degree:              %f" % min_degree(nodes))
        print("=== TEST ENDING ===\n")

    if args.draw:
        from generate_graphs import unit_disc_graph
        from charts import draw_nodes
        N = 1000
        nodes = unit_disc_graph(N, A)
        draw_nodes(nodes, topology="disc", num_nodes=N, output_dir="../results/disc/drawing/")
