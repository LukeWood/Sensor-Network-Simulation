from generate_graphs import unit_disc_graph
from generate_graphs import unit_square_graph
from time import process_time

A=64
Ns=[1000, 5000, 10000, 25000, 50000, 100000]

with open("../results/shared/generation_speeds.csv", "w+") as f:
    f.write("N,A,Square Time,Disc Time\n")
    for N in Ns:
        start = process_time()
        unit_disc_graph(N, A)
        end = process_time()
        disc_time = end - start

        start = process_time()
        unit_square_graph(N, A)
        end = process_time()
        square_time = end - start
        f.write("%d,%d,%f,%f\n" % (N, A, square_time, disc_time))
