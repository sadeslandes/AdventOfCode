import pathlib
import pytest

from aoc import solver


here = pathlib.Path(__file__).parent
input_files = sorted(here.glob("20*/*/*.txt"))


def get_id(input_file):
    return input_file.read_text().splitlines()[0] + f"_{input_file.stem[1:]}"


# @pytest.mark.timeout(60)
@pytest.mark.parametrize("input_file", input_files, ids=get_id)
def test_example(input_file, request):
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
    part1, part2 = solver(
        year,
        day,
        input_data,
        skip_part1=part1_answer == "-",
        skip_part2=part2_answer == "-"
    )

    # THEN
    if part1_answer != "-":
        assert str(part1) == part1_answer
    if part2_answer != "-":
        assert str(part2) == part2_answer
