file_path = "2019_day2.txt"
with open(file_path) as f:
    puzzle = f.read().split(",")

data = list(map(int, puzzle))

part1_data = data[:]
part1_data[1] = 12
part1_data[2] = 2

def intcode(input_data):
    data = input_data[:]
    for idx in range(0, len(data), 4):
        opcode = data[idx]
        first_p = data[idx + 1]
        second_p = data[idx + 2]
        third_p = data[idx + 3]
        if opcode == 1:
            data[third_p] = data[first_p] + data[second_p]
        elif opcode == 2:
            data[third_p] = data[first_p] * data[second_p]
        if opcode == 99:
            break
    return data[0]


part2_result = 0
for noun in range(100):
    for verb in range(100):
        data[1] = noun
        data[2] = verb

        output = intcode(data)

        if output == 19690720:
            part2_result = 100 * noun + verb
            break

print("part1 : {}".format(intcode(part1_data)))
print("part2 : {}".format(part2_result))
