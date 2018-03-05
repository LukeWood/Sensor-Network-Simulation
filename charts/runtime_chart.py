def runtime_chart(Ns, runtimes, graph_topology="", name=None, expected_order=1):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from .util import clear_chart
    clear_chart()
    sns.set_style("darkgrid")
    plt.title("Runtime for Graph Generation on the Shape: %s" % graph_topology)
    daters = pd.DataFrame(data={'N': Ns, 'runtimes': runtimes})
    sns.regplot('N', 'runtimes', data=daters, order=expected_order)
    plt.xlabel("Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    if name:
        plt.savefig(name, bbox_inches="tight")
    else:
        plt.show()
