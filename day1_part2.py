"""
리스트에서 3개의 합이 2020인 수의 곱
"""

file_path = "/venvs/adventofcode.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = list(map(int, line))

for i in range(len(lst)):
    for j in range(len(lst[1:])):
        for k in range(len(lst[2:])):
            if lst[i] + lst[j] + lst[k] == 2020:
                print(lst[i] * lst[j] * lst[k])
