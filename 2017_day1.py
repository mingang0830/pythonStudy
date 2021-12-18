file_path = "2017_day1.txt"
with open(file_path) as f:
    numbers = f.read()

# print(numbers)
# 11 = 2
# 111 = 3
# 1112 = 3

# program progress
# -----
# parse -> data input, parse -> 9514845... -> [9, 5, 1, 4, 8, 4, 5 ...]
# process -> logic
# aggregate -> combine multiple logics // user, restaurant, delivery -> delivery_info -> user(who am i? / get_user()) + restaurant(where? / get_restaurant()) + delivery()
# print -> result out

def parse(file_path):
    with open(file_path) as f:
      numbers = f.read()  # "9514845..."

    result = []
    for n in numbers:
        result.append(int(n))
    return result

revised_numbers = parse(file_path)

sum = 0
for i in range(len(revised_numbers)):
    cur_num = numbers[i]
    pre_num = numbers[i-1]
    if cur_num == pre_num:
        sum += cur_num

print("part1 : {}".format(sum))

def parse2(file_path):
    "
    [9, 5, 1, 4, 8, 4, 5 ...] -> [9, 5, 1, 4, 8], [4, 5 ...]
    "
    result = parse(file_path)  # wrapper
    """
    outer(^left-wing^(prepare) inner ^right-wing(revise)^)
    def outer():
        ... <<- left wing
        def inner():
            ...
        inner = inner()
        ... <<- right wing
        return
    """
    half_position_of_result = len(result) // 2
    return result[:half_position_of_result], result[half_position_of_result:]

left_half = numbers[:len(numbers)//2]
right_half = numbers[len(numbers)//2:]
left_half, right_half = parse2(file_path)
# 123123 -> [123] [123] -> 246 -> 12
# 124123 -> [124] [123] -> 24 -> 6
def process2():
    sum = 0
    for i in range(len(numbers)//2):
        if left_half[i] == right_half[i]:
            sum2 += left_half[i] + right_half[i]
    return sum

print("part2 : {}".format(process2()))
