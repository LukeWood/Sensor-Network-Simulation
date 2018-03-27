def draw_nodes(nodes, topology="", num_nodes=0, output_dir=""):
    import matplotlib.pyplot as plt
    x = [node.dims[0] for node in nodes]
    y = [node.dims[1] for node in nodes]
    plt.scatter(x, y)

    plt.xlim((0, 1))
    plt.ylim((0, 1))
    plt.title("RGG with %s Topology, %d Nodes" % (topology, num_nodes))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("%snodes.png" % output_dir, bbox_inches="tight")
