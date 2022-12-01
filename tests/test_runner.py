import pathlib
from sys import gettrace

import pytest

from aoc import solver

here = pathlib.Path(__file__).parent
input_files = sorted(here.glob("20*/*/*.txt"))
timeout = 0 if "pydevd" in gettrace().__repr__() else 10  # no timeout if debugging


def get_id(input_file):
    return input_file.read_text().splitlines()[0] + f"_{input_file.stem[1:]}"


@pytest.mark.timeout(timeout)
@pytest.mark.parametrize("input_file", input_files, ids=get_id)
def test_run(input_file, request):
    # GIVEN
    lines = input_file.read_text().splitlines()
    if len(lines) < 4:
        pytest.fail(f"test data {input_file} is malformed")
    metadata, *lines, part1_answer, part2_answer = lines
    input_data = "\n".join(lines).rstrip()

    # invoke the entrypoint with a controlled input
    year, day = map(int, metadata.split("_"))

    if year == 2020 and day == 9:
        # special case because PREAMBLE_LEN differs between sample and actual
        from aoc.aoc2020.day9 import day9

        day9.PREAMBLE_LEN = 5

    # WHEN
    skip_part1, skip_part2 = part1_answer.startswith("-"), part2_answer.startswith("-")
    part1, part2 = solver(
        year, day, input_data, skip_part1=skip_part1, skip_part2=skip_part2
    )

    # THEN
    if not skip_part1:
        assert str(part1) == part1_answer
    if not skip_part2:
        assert str(part2) == part2_answer
