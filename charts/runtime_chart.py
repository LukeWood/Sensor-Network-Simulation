def runtime_chart(Ns, runtimes, graph_topology="", name=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from .util import clear_chart
    clear_chart()
    sns.set_style("darkgrid")
    plt.title("Runtime for Graph Generation on the Shape: %s" % graph_topology)
    plt.xlabel("Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.plot(runtimes)
    if name:
        plt.savefig(name, bbox_inches="tight")
    else:
        plt.show()
