from setuptools import find_packages, setup

setup(
    name="AdventOfCode",
    version="1.0",
    packages=find_packages(),
    entry_points={"adventofcode.user": ["sadeslandes = aoc:solver"]},
)
