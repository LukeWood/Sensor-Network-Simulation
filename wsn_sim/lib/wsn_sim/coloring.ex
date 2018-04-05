defmodule WSNSim.Coloring do

    def inner_gather_data(n, a, generation_fn) do
      adj_list = generation_fn.(n, a)

      {ordering, degrees_when_removed} = GraphColoring.ShortestVertexLast.generate_ordering(adj_list)
      coloring = GraphColoring.color_graph(ordering, adj_list)

      {adj_list, degrees_when_removed, coloring}
    end

    def gather_data(benchmark, n, a,topology, generation_fn) do
      {runtime, {adj_list, degrees_when_removed, coloring}} = :timer.tc(fn -> inner_gather_data(n, a, generation_fn) end)
      runtime = runtime/1_000_000

      max_deg = RGG.Util.degrees(adj_list) |> RGG.Util.max_degree()
      color_sizes = Enum.reduce(coloring, %{}, fn {_node, color}, acc ->
        Map.update(acc, color, 1,&(&1+1))
      end)
      largest_color = Enum.reduce(color_sizes, 0, fn {_color, size}, acc -> max(acc, size) end)

      max_removed = Enum.reduce(degrees_when_removed, 0, fn {_coloring, size}, acc -> max(acc, size) end)

      {benchmark, n, a, topology, max_deg, max_removed, largest_color, runtime}
    end

    def run_benchmark({benchmark, n, a, Square}), do: gather_data(benchmark, n, a,"Square", &RGG.unit_square/2)
    def run_benchmark({benchmark, n, a, Disc}), do: gather_data(benchmark, n, a,"Disc", &RGG.unit_disc/2)
    def run_benchmark({benchmark, n, a, Sphere}), do: gather_data(benchmark, n, a,"Sphere", &RGG.unit_sphere/2)

    def benchmark_coloring(filename) do
      WSNSim.benchmark_list() |>
        Enum.map( &run_benchmark/1 ) |>
        Enum.map( &Tuple.to_list/1   ) |>
        Enum.map( fn benchmark -> Enum.map benchmark, &Kernel.inspect/1   end ) |>
        prepend_headers(["Benchmark", "N", "A", "Topology", "Max Deg", "Max Removed","Largest Color", "Runtime"]) |>
        Enum.map( fn benchmark -> Enum.join(benchmark, ",") end ) |>
        Enum.join("\n") |>
        write_to(filename)
    end

    def prepend_headers(other, headers) do
      [headers | other]
    end

    def write_to(contents, filename) do
      {:ok, file} = File.open(filename, [:write])
      IO.binwrite file, contents
      File.close file
    end

end
