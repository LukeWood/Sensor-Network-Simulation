from generate_graphs import unit_square_graph
from generate_graphs import brute_force_unit_square_graph

Ns = [1000, 2000, 3000, 5000, 10000]
A = 64

for N in Ns:
    from time import process_time
    start = process_time()
    unit_square_graph(N, A)
    end = process_time()

    n_runtime = end - start

    start = process_time()
    brute_force_unit_square_graph(N, A)
    end = process_time()

    n_squared_runtime = end - start

    print("%d,%f,%f" % (N, n_runtime, n_squared_runtime))
