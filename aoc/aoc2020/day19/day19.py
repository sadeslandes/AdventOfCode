import re
from itertools import product
from os import path


def parse_rules(rules):
    def _parse_rule(key):
        if key not in expanded:
            definition = raw[key]

            if re.match(r'^"[ab]+"$', definition):
                expanded[key] = set(definition.replace('"', ""))
            else:
                matches = set()
                for alt in definition.split("|"):
                    alt = alt.strip()
                    dependencies = (_parse_rule(k) for k in alt.split(" "))
                    matches |= set("".join(p) for p in product(*dependencies))
                expanded[key] = matches
        return expanded[key]

    expanded = dict()
    raw = {k: v.strip() for k, v in (rule.split(":") for rule in rules)}

    for rule in raw:
        _parse_rule(rule)
    return expanded


# Part 1
def part1(inpt: str):
    rules_raw, messages = (g.splitlines() for g in inpt.split("\n\n"))
    rules = parse_rules(rules_raw)
    count = 0
    for msg in messages:
        if msg in rules["0"]:
            count += 1
    return count


# Part 2
def part2(inpt: str):
    ###
    # new rule 8 matches n occurrences of rule 42 (n > 0)
    # new rule 11 matches n occurrences of rule 42,
    #   followed by n occurrences of rule 31 (n > 0)
    # validate new rule 0 backwards by:
    #   checking for n occurrences of rule 31 at end of string
    #   then count m occurrences of rule 42 at beginning of string
    #   checking that m > n
    #   verifying there is nothing between the matches of rule 42 and rule 31
    ###
    rules_raw, messages = (g.splitlines() for g in inpt.split("\n\n"))
    rules = parse_rules(rules_raw)
    if '42' not in rules or '31' not in rules:
        return None
    rule42_re = f"(?:{'|'.join(rules['42'])})"
    rule31_re = f"(?:{'|'.join(rules['31'])})"
    p_r31 = re.compile(rule31_re)
    p_r42 = re.compile(rule42_re)
    p_r31_all_end = re.compile(f"{rule31_re}+$")
    p_r42_all = re.compile(f"{rule42_re}+")
    count = 0
    for msg in messages:
        if m := p_r31_all_end.search(msg):
            # rule 31 found at end of string. count occurrences
            r31_start = m.start()
            num_r31 = len(p_r31.findall(msg, r31_start))
            num_r42 = len(p_r42.findall(msg, 0, r31_start))
            if num_r31 < num_r42 and p_r42_all.fullmatch(msg, 0, r31_start):
                count += 1
    return count


if __name__ == "__main__":
    from aoc.utils import Timer
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        data = f.read()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")