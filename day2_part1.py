file_path = "/venvs/adventofcode_2.txt"
with open(file_path) as f:
    line = f.read().splitlines()

lst = []
for i in line:
    lst.append(i.split(": "))


def count(str):
    result = {}
    for ch in str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result


# data = []
# for ele in lst:
#     location, given_char = ele[0].split(" ")  # 15-16
#     location = location.split("-")
#
#     data.append({"min": int(location[0]),
#                  "max": int(location[1]),
#                  "given_char": given_char,
#                  "count": count(ele[1])})
#
# count = 0
# for datum in data:
#     current_given_char_count = datum["count"].get(datum["given_char"], 0)
#     if datum["min"] <= current_given_char_count <= datum["max"]:
#         count += 1
#
# print(count)

dict = {}
for idx, i in enumerate(lst):
    value = i[0].split()
    dict[idx] = [i[1], list(map(int, value[0].split("-"))), value[1]]

count = 0
for key, value in dict.items():
    if value[1][0] <= value[0].count(value[2]) <= value[1][1]:
        count += 1

print(count)
