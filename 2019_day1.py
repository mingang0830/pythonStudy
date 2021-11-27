file_path = "2019_day1.txt"
with open(file_path) as f:
    numbers = f.read().splitlines()


def calc(number):
    return int(int(number) / 3) - 2


print("part1 : {}".format(sum([calc(number) for number in numbers])))

lst2 = []
for num in numbers:
    cur_num = num
    while True:
        result = calc(cur_num)
        if result <= 0:
            break
        lst2.append(result)
        cur_num = result

print("part2 : {}".format(sum(lst2)))
