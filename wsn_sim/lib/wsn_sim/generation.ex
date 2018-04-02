defmodule WSNSim.Generation do
    def gather_data(benchmark, n, a, generation_fn) do
      {runtime, nodes} = :timer.tc(fn -> generation_fn.(n, a) end)
      runtime = runtime/1_000_000
      degrees = RGG.Util.degrees(nodes)
      avg_deg = RGG.Util.average_degree(degrees)
      max_deg = RGG.Util.max_degree(degrees)
      min_deg = RGG.Util.min_degree(degrees)

      {benchmark, n, a, avg_deg, max_deg, min_deg, runtime}
    end

    def run_benchmark({benchmark, n, a, Square}), do: gather_data(benchmark, n, a, &RGG.unit_square/2)
    def run_benchmark({benchmark, n, a, Disc}), do: gather_data(benchmark, n, a, &RGG.unit_disc/2)
    def run_benchmark({benchmark, n, a, Sphere}), do: gather_data(benchmark, n, a, &RGG.unit_sphere/2)

    def benchmark_generation(filename) do
      WSNSim.benchmark_list() |>
        Enum.map(
          &run_benchmark/1
        ) |>
        Enum.map(
          &Tuple.to_list/1
        ) |>
        Enum.map(
          fn benchmark ->
            Enum.map benchmark, &Kernel.inspect/1
          end
        ) |>
        prepend_headers(["Benchmark", "N", "A", "Avg. Deg", "Max Deg", "Min Deg", "Second"]) |>
        Enum.map(
          fn benchmark ->
            Enum.join(benchmark, ",")
          end
        ) |>
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
