file_path = "2017_day1.txt"
with open(file_path) as f:
    numbers = f.read()

# print(numbers)
sum = 0
for i in range(len(numbers)):
    cur_num = numbers[i]
    pre_num = numbers[i-1]
    if cur_num == pre_num:
        sum += int(cur_num)

print("part1 : {}".format(sum))

sum2 = 0
left_half = numbers[:len(numbers)//2]
right_half = numbers[len(numbers)//2:]

for i in range(len(numbers)//2):
    if left_half[i] == right_half[i]:
        sum2 += int(left_half[i]) + int(right_half[i])

print("part2 : {}".format(sum2))
