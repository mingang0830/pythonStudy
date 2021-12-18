file_path = "2017_day2.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


def max_min(data):
    max_ = max(data)
    min_ = min(data)
    return max_ - min_


def div(data):
    for i in range(len(data)):
        for j in range(len(data)):
            
            if data[i] % data[j] == 0:
                return data[i] / data[j]
            elif data[j] % data[i] == 0:
                return data[j] / data[i]
# [1 2 3 4 5 6]
# (1 2), (1 3), (1 4), (1 5), (1 6)
# (2 3), (2 4), (2 5), (2 6)
# ...

# [1 2 3 4 5 6]
#->
# (1 1) (1 2) (1 3) (1 4) ...
# (2 1) (2 2) (2 3) (2 4) ...
# ...
# [(1 1), (1 2), (1 3) ... (2 1), (2 2), (2 3), ...]
# filter (same elements of pair)
#->
# (1 2), (1 3), (1 4), (1 5), (1 6)
# (2 1), (2 3), (2 4), (2 5), (2 6)
# (3 1), (3 2), (3 4), (3 5), (3 6)
# (4 1), (4 2), (4 3), (4 5), (4 6)
# ...

part1 = 0
part2 = 0
for line in puzzle:
    data = list(map(int, line.split("\t")))
    part1 += max_min(data)
    part2 += div(data)

print("part1 : {}".format(part1))
print("part2 : {}".format(part2))