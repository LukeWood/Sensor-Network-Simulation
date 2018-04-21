headers = ["Benchmark","N","A","R","Topology","Avg. Degree","Min Degree",
    "Max Degree","Average Degree When Removed","Colors","Largest Color",
    "Backbone Order","Backbone Size","Backbone Domination",
    "Number of Backbone Faces",
    "Generation Runtime", "Coloring Runtime", "Backbone Runtime", "Total Runtime"]

benchmark_indices = {
    "generation": ["Benchmark", "N", "A", "Topology", "Avg. Degree", "Min Degree", "Max Degree", "Generation Runtime"],
    "coloring": ["Benchmark", "N", "A", "Topology", "Average Degree When Removed", "Colors", "Largest Color", "Coloring Runtime"],
    "backbones": ["Benchmark", "N", "A", "Topology", "Backbone Order", "Backbone Size", "Backbone Domination", "Number of Backbone Faces", "Backbone Runtime"]
}

benchmark_data = {}
for col in headers:
    benchmark_data[col] = []

with open("../results/benchmarks/full_benchmark.csv") as f:
    for line in f:
        spl = line.split(",")
        for index, item in enumerate(spl):
            benchmark_data[headers[index]].append(item)


for benchmark_name, indices in benchmark_indices.items():
    file_name = "../results/benchmarks/%s_benchmark.csv" % benchmark_name
    columns = [benchmark_data[index] for index in indices]
    with open(file_name, "w+") as f:
        for index in range(len(columns[0])):
            f.write(",".join([x[index] for x in columns]) + "\n")
        f.flush()
