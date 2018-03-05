def edge_density_histogram(degrees, max_degree, graph_topology="", name=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from .util import clear_chart
    clear_chart()

    yvals = [0 for _ in range(max_degree+1)]
    for d in degrees:
        yvals[d] = yvals[d] + 1
    ax = sns.barplot(x=list(range(max_degree+1)), y=yvals)
    plt.title("Degree Distribution for %d Nodes on the Shape: %s" % (len(degrees), graph_topology))
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    if name:
        plt.savefig(name, bbox_inches="tight")
    else:
        plt.show()
