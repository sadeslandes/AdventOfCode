from os import path


def parse_input(inpt):
    rules_raw, my_ticket_raw, other_tickets_raw = inpt.split("\n\n")
    # parse rules
    rules_dict = dict()
    for line in rules_raw.splitlines():
        line = line.replace(" ", "")
        field, rules_str = line.split(":")
        rules = rules_str.split("or")
        ranges = [tuple(int(n) for n in rnge.split("-")) for rnge in rules]
        rules_dict[field] = ranges
    # parse my ticket
    my_ticket = [int(n) for n in my_ticket_raw.splitlines()[1].split(",")]
    # other tickets
    other_tickets_str = other_tickets_raw.splitlines()[1:]
    other_tickets = [[int(n) for n in t.split(",")] for t in other_tickets_str]

    return rules_dict, my_ticket, other_tickets


def validate_value(value, rules, rule):
    return any(r[0] <= value <= r[1] for r in rules[rule])


def validate_ticket(rules, ticket):
    invalid = []
    for value in ticket:
        valid = False
        for rule in rules:
            if validate_value(value, rules, rule):
                valid = True
        if not valid:
            invalid.append(value)
    return (len(invalid) == 0, invalid)


def constrain_fields(fields):
    propagated = set()
    while not all(len(f) == 1 for f in fields.values()):
        for name, values in fields.items():
            val = next(iter(values))
            if len(values) == 1 and val not in propagated:
                propagated.add(val)
                for f2 in fields:
                    if f2 != name:
                        try:
                            fields[f2].remove(val)
                        except KeyError:
                            pass
    return {f: next(iter(v)) for f, v in fields.items()}


# Part 1
def part1(inpt: str):
    rules, _, other_tickets = parse_input(inpt)
    invalid = []
    for ticket in other_tickets:
        _, invalid_values = validate_ticket(rules, ticket)
        invalid.extend(invalid_values)
    return sum(invalid)


# Part 2
def part2(inpt: str):
    rules, my_ticket, other_tickets = parse_input(inpt)
    valid = [t for t in other_tickets if validate_ticket(rules, t)[0]]
    transposed = [list(z) for z in zip(*valid)]
    fields = dict()
    for rule in rules:
        for pos, values in enumerate(transposed):
            if all(validate_value(value, rules, rule) for value in values):
                fields.setdefault(rule, set()).add(pos)
    fields = constrain_fields(fields)

    result = 1
    for field in fields:
        if field.startswith("departure"):
            result *= my_ticket[fields[field]]
    return result


if __name__ == "__main__":
    from aoc.utils import Timer

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        data = f.read()
    with Timer() as t1:
        p1 = part1(data)
    print(f"Part 1: {t1} {p1}")
    with Timer() as t2:
        p2 = part2(data)
    print(f"Part 2: {t2} {p2}")
