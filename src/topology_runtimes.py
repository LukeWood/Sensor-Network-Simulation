from generate_graphs import unit_square_graph
from generate_graphs import unit_disc_graph
from generate_graphs import unit_sphere_graph

from time import process_time

def time_run(fn, N, A):
    start = process_time()
    fn(N, A)
    end = process_time()
    return end - start

A=64
Ns=[1000, 5000, 10000, 25000, 50000, 100000]

with open("../results/shared/generation_speeds.csv", "w+") as f:
    f.write("N,A,Square Runtime,Disc Runtime,Sphere Runtime\n")
    for N in Ns:
        square_time = time_run(unit_square_graph, N, A)
        disc_time = time_run(unit_disc_graph, N, A)
        sphere_time = time_run(unit_sphere_graph, N, A)

        f.write("%d,%d,%f,%f,%f\n" % (N, A, square_time, disc_time, sphere_time))
