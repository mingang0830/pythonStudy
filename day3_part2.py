file_path = "/venvs/adventofcode_3.txt"
with open(file_path) as f:
    line = f.read().splitlines()


def count_trees(right, down):
    tree = 0
    a = 0
    b = len(line[0])

    for i in range(0, len(line), down):
        if line[i][a] == "#":
            tree += 1
        a = (a + right) % b

    return tree


print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
