file_path = "2018_day1.txt"
with open(file_path) as f:
    str_lst = f.read().splitlines()


def int_numbers(str_list):
    return [int(i) for i in str_list]


print("part1 : {}".format(sum(int_numbers(str_lst))))

# [+1 -2 +3 -4 +5 ...]
# [1 -1 2 -2 3 ...]

def part2():
    cur_sum = 0
    sum_list = []
    while True:
        for number in int_numbers(str_list)
            cur_sum += number
            sum_list.append(cur_sum)
            if sum_list.count(cur_sum) == 2:
                return cur_sum


sum = 0
sum_lst = []
for i in int_numbers(str_lst):
    sum += i
    sum_lst.append(sum)
# [0 1 3 6 10 15]
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
