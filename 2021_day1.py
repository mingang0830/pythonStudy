file_path = "2021_day1.txt"
with open(file_path) as f:
    report_str = f.read().splitlines()


def int_numbers(str_list):
    return [int(i) for i in str_list]


report = int_numbers(report_str)
report_len = len(report)

increased_1 = 0
for idx in range(report_len):
    cur_idx = idx
    next_idx = idx + 1
    if next_idx == report_len:
        break
    if report[cur_idx] < report[next_idx]:
        increased_1 += 1

print("part1 : {}".format(increased_1))

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
