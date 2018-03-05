def runtime_chart(Ns, runtimes, graph_topology="", name=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from .util import clear_chart
    clear_chart()
    sns.set_style("darkgrid")
    plt.title("Runtime for Graph Generation on the Shape: %s" % graph_topology)
    plt.xlabel("Nodes")
    plt.ylabel("Runtime (seconds)")
    daters = pd.DataFrame(data={'N': Ns, 'runtimes': runtimes})
    sns.lmplot('N', 'runtimes', data=daters)
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    if name:
        plt.savefig(name, bbox_inches="tight")
    else:
        plt.show()
