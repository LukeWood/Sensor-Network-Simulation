#!/bin/sh
cd lib
pip install -e .
cd ..
mkdir results
cd results
mkdir backbone
mkdir benchmarks
mkdir comparison
mkdir disc
mkdir generation
mkdir python
mkdir square
mkdir sphere
mkdir walkthrough
cd ..
cd main_drivers
python benchmarks.py
python subtables.py
python walkthrough.py
python color_set_size_distribution.py
python random_coloring_vs_slvo.py
python sequential_coloring_plot.py
