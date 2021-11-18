file_path = "/venvs/adventofcode_2.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = []
for i in line:
    lst.append(i.split(": "))

dict = {}
for idx, i in enumerate(lst):
    value = i[0].split()
    dict[idx] = [i[1], list(map(int, value[0].split("-"))), value[1]]

count = 0
for key, value in dict.items():
    if value[1][0] <= value[0].count(value[2]) <= value[1][1]:
        count += 1

print(count)
