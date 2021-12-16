file_path = "2017_day2.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


def max_min(data):
    max_ = max(data)
    min_ = min(data)
    return max_ - min_


def div(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] % data[j] == 0:
                return data[i] / data[j]
            elif data[j] % data[i] == 0:
                return data[j] / data[i]


part1 = 0
part2 = 0
for line in puzzle:
    data = list(map(int, line.split("\t")))
    part1 += max_min(data)
    part2 += div(data)


print("part1 : {}".format(part1))
print("part2 : {}".format(part2))