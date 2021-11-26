file_path = "/venvs/adventofcode_2.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = []
for i in line:
    lst.append(i.split(": "))

data = []
for ele in lst:
    locations, given_char = ele[0].split(" ")
    first, second = locations.split("-")
    data.append({"first": int(first) - 1,
                 "second": int(second) - 1,
                 "given_char": given_char,
                 "given_string": ele[1]})

count = 0
for datum in data:
    first_position_char = datum["given_string"][datum["first"]]
    second_position_char = datum["given_string"][datum["second"]]
    if first_position_char == datum["given_char"] and second_position_char != datum["given_char"]:
        count += 1
    elif second_position_char == datum["given_char"] and first_position_char != datum["given_char"]:
        count += 1

print(count)

dict = {}
for idx, i in enumerate(lst):
    value = i[0].split()
    dict[idx] = [i[1], list(map(int, value[0].split("-"))), value[1]]


count = 0

for key, value in dict.items():
    first_position_letter = value[0][value[1][0] - 1]
    second_position_letter = value[0][value[1][1] - 1]
    given_letter = value[2]

    # if first_position_letter == given_letter:
    #     if not second_position_letter == given_letter:
    #         count += 1
    # elif second_position_letter == given_letter:
    #     count += 1

    if first_position_letter == given_letter and not second_position_letter == given_letter:
        count += 1
    elif second_position_letter == given_letter and not first_position_letter == given_letter:
        count += 1
print(count)

