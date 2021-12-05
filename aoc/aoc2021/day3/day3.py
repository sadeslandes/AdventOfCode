from os import path


# Part 1
def part1(inpt: str):
    inpt_lines = inpt.splitlines()
    transposed = transpose(inpt_lines)
    gamma_rate = int("".join(most_common_bit(row) for row in transposed), 2)
    epsillon_rate = int("1" * len(transposed), 2) - gamma_rate
    return epsillon_rate * gamma_rate


# Part 2
def part2(inpt: str):
    inpt_lines = inpt.splitlines()
    O2_generator_rating = get_rating(inpt_lines, most_common_bit)
    CO2_scrubber_rating = get_rating(inpt_lines, least_common_bit)
    return O2_generator_rating * CO2_scrubber_rating


def get_rating(values, bit_criteria, idx=0):
    if len(values) == 1:
        return int(values[0], 2)
    bit_criteria_val = bit_criteria(transpose(values)[idx])
    new_values = filter(lambda v: v[idx] == bit_criteria_val, values)
    return get_rating(list(new_values), bit_criteria, idx + 1)


def transpose(str_array):
    if not str_array:
        return []
    num_bits = len(str_array[0])
    return ["".join(row[i] for row in str_array) for i in range(num_bits)]


def most_common_bit(binary_str):
    return "0" if binary_str.count("0") > len(binary_str) // 2 else "1"


def least_common_bit(binary_str):
    return "0" if most_common_bit(binary_str) == "1" else "1"


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        inpt = f.read()
    print(f"Part 1: {part1(inpt)}")
    print(f"Part 2: {part2(inpt)}")
