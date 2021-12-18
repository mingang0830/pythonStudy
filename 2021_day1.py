file_path = "2021_day1.txt"
with open(file_path) as f:
    report_str = f.read().splitlines()


def int_numbers(str_list):
    return [int(i) for i in str_list]


report = int_numbers(report_str)
report_len = len(report)
# [1 2 3 4 5] -> 5 == len(..) = 5 - 1 = 4
# [1 3 2 4 5] -> 3
increased_1 = 0
for idx in range(report_len - 1):
    cur_idx = idx
    next_idx = idx + 1
    if report[cur_idx] < report[next_idx]:
        increased_1 += 1

print("part1 : {}".format(increased_1))
# [1 2 3 4 5 6] 1+2+3 < 2+3+4 -> +1
increased_2 = 0
for idx in range(report_len):
    first_idx = idx
    second_idx = idx + 1
    third_idx = idx + 2
    if third_idx + 1 == report_len:
        break
    if report[first_idx] + report[second_idx] + report[third_idx] < report[first_idx + 1] + report[second_idx + 1] + report[third_idx + 1]:
        increased_2 += 1

print("part2 : {}".format(increased_2))
