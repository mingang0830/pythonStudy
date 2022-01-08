file_path = "2021_day3.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()

bit_count = {}
gamma_rate = []
epsilon_rate = []

for bits in puzzle:
    for position, bit in enumerate(bits):
        if position not in bit_count:
            if bit == "0":
                bit_count[position] = {"0": 1, "1": 0}
            elif bit == "1":
                bit_count[position] = {"0": 0, "1": 1}
        else:
            if bit == "0":
                bit_count[position]["0"] += 1
            elif bit == "1":
                bit_count[position]["1"] += 1


for position, number in bit_count.items():
    if number["0"] > number["1"]:
        gamma_rate.append("0")
        epsilon_rate.append("1")
    else:
        gamma_rate.append("1")
        epsilon_rate.append("0")


def decimal(binary):
    return int("0b" + "".join(binary), 2)


gamma_rate_in_decimal = decimal(gamma_rate)
epsilon_rate_in_decimal = decimal(epsilon_rate)

print("part 1 : {}".format(gamma_rate_in_decimal * epsilon_rate_in_decimal))


def o2_rating(report):
    zero_bits = []
    one_bits = []

    for i in range(len(report[0])):
        for j in report:
            if j[i] == '0':
                zero_bits.append(j)
            elif j[i] == '1':
                one_bits.append(j)

        if len(zero_bits) > len(one_bits):
            report = zero_bits
        elif len(zero_bits) < len(one_bits):
            report = one_bits
        elif len(zero_bits) == len(one_bits):
            report = one_bits

        if len(report) == 1:
            return report

        zero_bits, one_bits = [], []


def co2_rating(report):
    zero_bits = []
    one_bits = []

    for i in range(len(report[0])):
        for j in report:
            if j[i] == '0':
                zero_bits.append(j)
            elif j[i] == '1':
                one_bits.append(j)

        if len(zero_bits) < len(one_bits):
            report = zero_bits
        elif len(zero_bits) > len(one_bits):
            report = one_bits
        elif len(zero_bits) == len(one_bits):
            report = zero_bits

        if len(report) == 1:
            return report

        zero_bits, one_bits = [], []


print("part2 : {}".format(decimal(o2_rating(puzzle)) * decimal(co2_rating(puzzle))))








