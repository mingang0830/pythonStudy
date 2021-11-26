file_path = "2019_day1.txt"
with open(file_path) as f:
    numbers = f.read().splitlines()


def calc(number):
    return int(int(number) / 3) - 2


print("part1 : {}".format(sum([calc(number) for number in numbers])))


lst2 = []
# for number2 in numbers:
#     num = calc(number2)
#     lst2.append(num)
#     while True:
#         if num > 6:
#             num = calc(num)
#             lst2.append(num)
#         else:
#             break

for number2 in numbers:
    sum_number = 0
    num = calc(number2)
    sum_number += num
    while True:
        if num > 6:
            num = calc(num)
            sum_number += num
        else:
            lst2.append(sum_number)
            break

print("part2 : {}".format(sum(lst2)))
