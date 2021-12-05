import importlib


def solver(year, day, data, skip_part1=False, skip_part2=False):
    mod_name = f"aoc.aoc{year}.day{day}.day{day}"
    mod = importlib.import_module(mod_name)
    part1 = part2 = None
    if not skip_part1:
        part1 = mod.part1(data)
    if not skip_part2:
        part2 = mod.part2(data)
    return part1, part2
