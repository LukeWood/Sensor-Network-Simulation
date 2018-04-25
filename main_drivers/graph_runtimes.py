from rgg.generate_graphs import unit_square_graph
from rgg.generate_graphs import unit_disc_graph
from rgg.generate_graphs import unit_sphere_graph

from time import process_time

def time_run(fn, N, A):
    start = process_time()
    fn(N, A)
    end = process_time()
    return end - start

A=64
Ns=[10, 1000, 2500, 5000, 16000, 32000, 64000]

def runtime_chart(Ns, runtimes, name=None, expected_order=1):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    sns.set_style("darkgrid")
    daters = pd.DataFrame(data={'N': Ns, 'runtimes': runtimes})
    sns.regplot('N', 'runtimes', data=daters, order=expected_order)
    plt.xlabel("Nodes")
    plt.ylabel("Runtime (seconds)")

runtimes_square = [time_run(unit_square_graph, N, A) for N in Ns]
runtimes_disc = [time_run(unit_disc_graph, N, A) for N in Ns]
runtimes_sphere = [time_run(unit_sphere_graph, N, A) for N in Ns]

runtime_chart(Ns, runtimes_square)
runtime_chart(Ns, runtimes_disc)
runtime_chart(Ns, runtimes_sphere)

plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)

import matplotlib.pyplot as plt
plt.title("Runtimes for All Topologies")
plt.savefig("../results/comparison/running_times.png", bbox_inches="tight")
