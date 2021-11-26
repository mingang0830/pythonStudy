file_path = "/venvs/adventofcode_3.txt"
with open(file_path) as f:
    lines = f.read().splitlines()


def count_trees_1(x, y):
    count = 0
    pos = {"x": 0, "y": 0}
    max_x, max_y = len(lines[0]), len(lines)
    for line in range(0, len(lines), y):
        if lines[pos["y"]][pos["x"]] == "#":
            count += 1

        pos["x"] = (pos["x"] + x) % max_x
        pos["y"] = (pos["y"] + y) % max_y
    return count




if __name__ == "__main__":
    print(count_trees_1(3, 1))
#     print(count_trees_1(3, 1))
#
#     tree = 0
#     a = 0
#     b = len(lines[0])
#
#     for i in range(len(lines)):
#         if lines[i][a] == "#":
#             tree += 1
#         a = (a + 3) % b  # 세칸씩 오른쪽으로 넘어가면서 범위를 벗어날 경우를 위해 길 길이를 나눈 나머지 만큼 넘어가기
#
#     print(tree)
