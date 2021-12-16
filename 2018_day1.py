file_path = "2018_day1.txt"
with open(file_path) as f:
    str_lst = f.read().splitlines()


def int_numbers(str_list):
    return [int(i) for i in str_list]


print("part1 : {}".format(sum(int_numbers(str_lst))))

sum = 0
sum_lst = []
for i in int_numbers(str_lst):
    sum += i
    sum_lst.append(sum)

a = 0
breaker = True
while True:
    for i in int_numbers(str_lst):
        sum_lst.append(sum_lst[-1] + i)
        if sum_lst.count(sum_lst[-1]) == 2:
            breaker = False
            break
    if breaker is False:
        break

print("part2 : {}".format(sum_lst[-1]))
