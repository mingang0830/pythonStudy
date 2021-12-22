file_path = "2018_day2.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


two_chars = []
three_chars = []
count_two = 0
count_three = 0
# abcdedgad
# 1*1 = 1
# for row in puzzle:
    # row == "aaaaaaaab"
    #[1 2 3 4 4] -> set([1 2 3 4 4]) -> [1 2 3 4]
    #"aaaaaaaab" -> set("aaaaaaaab") -> ["a" "b"]
    #{"keys": "value"}
    # "abbbcccddd" -> {"a": 1, "b": 3, "c": 4, "d": 5}
    # result = {}
    # for ch in row:
    #     if ch not in result:
    #         result[ch] = 1
    #     else:
    #         result[ch] += 1
    #
    # for k, v in result.items():
    #     if v == 2:
    #         count_two += 1
    #     elif v == 3:
    #         count_three += 1

for i in puzzle:
    for j in i:
        if i.count(j) == 2:
            two_chars.append(j)
        elif i.count(j) == 3:
            three_chars.append(j)

    if len(two_chars) != 0:
        count_two += 1
        two_chars = []
    if len(three_chars) != 0:
        count_three += 1
        three_chars = []

print("part1 : {}".format(count_two * count_three))


def compare(str1, str2):
    result_count = 0
    for ele1, ele2 in zip(str1, str2):
        if ele1 == ele2:
            result_count += 1
    return result_count


def is_one_character_diffrent(str1, str2):
    return len(str1) == compare(str1, str2) + 1


def same_chars(str1, str2):
    result_letters_lst = []
    for ele1, ele2 in zip(str1, str2):
        if ele1 == ele2:
            result_letters_lst.append(ele1)
    return "".join(result_letters_lst)


result_letters = None
pairs = []
for str1_idx in range(len(puzzle)):
    for str2_idx in range(str1_idx+1, len(puzzle)):
        pairs.append((puzzle[str1_idx], puzzle[str2_idx]))

for str1, str2 in pairs:
    if is_one_character_diffrent(str1, str2):
        result_letters = same_chars(str1, str2)

print("part2 : {}".format(result_letters))


