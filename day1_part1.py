file_path = "/venvs/adventofcode.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = list(map(int, line))


for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[i] + lst[j] == 2020:
            print(lst[i] * lst[j])

