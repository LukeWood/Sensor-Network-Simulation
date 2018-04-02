defmodule WSNSim do

  def benchmark_list do
    [
      {1, 1000, 32, Square},
      {2, 8000, 64, Square},
      {3, 16000, 32, Square},
      {4, 64000, 64, Square},
      {5, 64000, 128, Square},
      {6, 128_000, 64, Square},
      {7, 128_000, 128, Square},
      {8, 8000, 64, Disc},
      {9, 64000, 64, Disc},
      {10, 64000, 128, Disc},
      {11, 16000, 64, Sphere},
      {12, 32000, 128, Sphere},
      {13, 64000, 128, Sphere}
    ]
  end

  def gather_data(benchmark, n, a, generation_fn) do
    {runtime, nodes} = :timer.tc(fn -> RGG.unit_square(n, a) end)
    degrees = RGG.Util.degrees(nodes)
    avg_deg = RGG.Util.average_degree(degrees)
    max_deg = RGG.Util.max_degree(degrees)
    min_deg = RGG.Util.min_degree(degrees)

    {benchmark, n, a, avg_deg, max_deg, min_deg, runtime}
  end

  def run_benchmark(benchmark, n, a, Square) do
    gather_data(benchmark, n, a, &RGG.unit_square/2)
  end
  def run_benchmark(benchmark, n, a, Disc) do
    gather_data(benchmark, n, a, &RGG.unit_disc/2)
  end
  def run_benchmark(benchmark, n, a, Sphere) do
    gather_data(benchmark, n, a, &RGG.unit_sphere/2)
  end

  def run_all_benchmarks do

  end

end
