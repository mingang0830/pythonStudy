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

gamma_rate_in_decimal = int("0b" + "".join(gamma_rate), 2)
epsilon_rate_in_decimal = int("0b" + "".join(epsilon_rate), 2)

print("part 1 : {}".format(gamma_rate_in_decimal * epsilon_rate_in_decimal))







