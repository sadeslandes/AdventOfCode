import re
from os import path

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def validate_birthyear(n):
    return 1920 <= int(n) <= 2002


def validate_issueyear(n):
    return 2010 <= int(n) <= 2020


def validate_expyear(n):
    return 2020 <= int(n) <= 2030


def validate_height(h):
    unit = h[-2:]
    if unit == "in":
        return 59 <= int(h[:-2]) <= 76
    if unit == "cm":
        return 150 <= int(h[:-2]) <= 193
    return False


def validate_haircolor(c):
    return re.match(r"#[0-9a-f]{6}$", c) is not None


def validate_eyecolor(c):
    return c in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(n):
    return len(n) == 9


def validate_cid(n):
    return True


validations = {
    "byr": validate_birthyear,
    "iyr": validate_issueyear,
    "eyr": validate_expyear,
    "hgt": validate_height,
    "hcl": validate_haircolor,
    "ecl": validate_eyecolor,
    "pid": validate_pid,
    "cid": validate_cid,
}


def split_passports(inpt):
    return [passport.replace("\n", " ") for passport in inpt.split("\n\n")]


def parse_passport(passport_str):
    passport_props = passport_str.strip().split(" ")
    return {k: v for k, v in (prop.split(":") for prop in passport_props)}


# Part 1
def part1(inpt: str):
    passports = split_passports(inpt)
    valid = 0
    for p in passports:
        passport = parse_passport(p)
        missing_fields = fields - set(passport.keys())
        if missing_fields == set() or missing_fields == {"cid"}:
            valid += 1
    return valid


# Part 2
def part2(inpt: str):
    passports = split_passports(inpt)
    valid = 0
    for p in passports:
        passport = parse_passport(p)
        missing_fields = fields - set(passport.keys())
        if missing_fields == set() or missing_fields == {"cid"}:
            if all(validations[k](v) for k, v in passport.items()):
                valid += 1
    return valid


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
