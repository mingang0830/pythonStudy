from day3_part1 import count_trees_1

file_path = "/venvs/adventofcode_3.txt"
with open(file_path) as f:
    line = f.read().splitlines()

pos_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = []
for x, y in pos_list:
    counts.append(count_trees_1(x, y))


result = 1
for count in counts:
    result *= count

print(result)


# def count_trees(right, down):
#     tree = 0
#     a = 0
#     b = len(line[0])
#
#     for i in range(0, len(line), down):
#         if line[i][a] == "#":
#             tree += 1
#         a = (a + right) % b
#
#     return tree
#
#
# print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))

