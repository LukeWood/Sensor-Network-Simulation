def edge_density_histogram(degrees, max_degree, graph_shape="", name=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.clf()
    plt.cla()
    plt.close()
    sns.distplot(degrees)
    plt.xlim(0, max_degree)
    plt.title("Degree Distribution for %d Nodes on the Shape: %s" % (len(degrees), graph_shape))
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    if name:
        plt.savefig(name, bbox_inches="tight")
    else:
        plt.show()
