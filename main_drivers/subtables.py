headers = ["Benchmark","N","A","R","Topology","Num Edges","Avg. Degree","Min Degree",
    "Max Degree","Average Degree When Removed","Colors","Largest Color", "Terminal Clique Size",
    "Backbone Order","Backbone Size","Backbone Domination",
    "Number of Backbone Faces",
    "Generation Runtime (Seconds)", "Coloring Runtime (Seconds)", "Backbone Runtime (Seconds)", "Total Runtime (Seconds)"]

benchmark_indices = {
    "generation": ["Benchmark", "N", "A", "Topology","Num Edges", "Avg. Degree", "Min Degree", "Max Degree", "Generation Runtime (Seconds)"],
    "coloring": ["Benchmark", "N", "A", "Topology", "Average Degree When Removed", "Colors", "Largest Color", "Terminal Clique Size", "Coloring Runtime (Seconds)"],
    "backbones": ["Benchmark", "N", "A", "Topology", "Backbone Order", "Backbone Size", "Backbone Domination", "Number of Backbone Faces", "Backbone Runtime (Seconds)"],
    "summary": ["Benchmark", "N", "A", "Topology", "Generation Runtime (Seconds)", "Coloring Runtime (Seconds)", "Backbone Runtime (Seconds)", "Total Runtime (Seconds)"]
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
