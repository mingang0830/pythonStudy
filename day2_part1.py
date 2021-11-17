file_path = "/venvs/adventofcode_2.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = []
for i in line:
    lst.append(i.split(": "))

dict = {}
for i in lst:
    value = i[0].split()
    dict[i[1]] = [list(map(int, value[0].split("-"))), value[1]]


count = 0
for key, value in dict.items():
    if value[0][0] <= key.count(value[1]) <= value[0][1]:
        count += 1
        print(value, key, count)


