from generate_graph import unit_square_graph

adjacency_list, radius, total_edges, average_degree, max_degree, min_degree, edge_distribution = unit_square_graph(100, 10)

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(edge_distribution)
plt.show()
