file_path = "2019_day3.txt"
with open(file_path) as f:
    puzzle = f.read().split("\n")

first_path = puzzle[0].split(",")
second_path = puzzle[1].split(",")


def move(path):
    wire_path = []
    x = 0
    y = 0
    for dir_ in path:
        if dir_[0] == 'R':
            for step in range(int(dir_[1:])):
                x += 1
                wire_path.append((x, y))
        elif dir_[0] == 'L':
            for step in range(int(dir_[1:])):
                x -= 1
                wire_path.append((x, y))
        elif dir_[0] == 'U':
            for step in range(int(dir_[1:])):
                y += 1
                wire_path.append((x, y))
        elif dir_[0] == 'D':
            for step in range(int(dir_[1:])):
                y -= 1
                wire_path.append((x, y))

    return wire_path


def find_closest_point(intersection_points):
    distance = []
    for point in intersection_points:
        distance.append(abs(point[0]) + abs(point[1]))

    return min(distance)


intersection_points = set(move(first_path)) & set(move(second_path))
print("part1 : {}".format(find_closest_point(intersection_points)))
