from generate_graphs import unit_sphere_graph
from charts import scatterplot3D
N = 1000
A = 64
nodes = unit_sphere_graph(N, A)

scatterplot3D(nodes)
