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

end
