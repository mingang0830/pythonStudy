file_path = "/venvs/adventofcode_3.txt"
with open(file_path) as f:
    line = f.read().splitlines()


tree = 0
a = 0
b = len(line[0])

for i in range(len(line)):
    if line[i][a] == "#":
        tree += 1
    a = (a + 3) % b  # 세칸씩 오른쪽으로 넘어가면서 범위를 벗어날 경우를 위해 길 길이를 나눈 나머지 만큼 넘어가기

print(tree)
