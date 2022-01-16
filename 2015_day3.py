file_path = "2015_day3.txt"
with open(file_path) as f:
    puzzle = f.read()

x, y = 0, 0
house_location = []
house_location2 = []


def move(dir_, x, y):
    if dir_ == "^":
        y += 1
    elif dir_ == "v":
        y -= 1
    elif dir_ == "<":
        x -= 1
    elif dir_ == ">":
        x += 1
    return x, y


for dir_ in puzzle:
    x, y = move(dir_, x, y)
    house_location.append((x, y))


santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
for idx in range(0, len(puzzle) - 1, 2):
    santa_dir = puzzle[idx]
    robo_dir = puzzle[idx + 1]

    santa_x, santa_y = move(santa_dir, santa_x, santa_y)
    house_location2.append((santa_x, santa_y))

    robo_x, robo_y = move(robo_dir, robo_x, robo_y)
    house_location2.append((robo_x, robo_y))

print("part1 : {}".format(len(set(house_location))))
print("part2 : {}".format(len(set(house_location2))))




