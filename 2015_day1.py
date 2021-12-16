file_path = "2015_day1.txt"
with open(file_path) as f:
    directions = f.read()


def positions(directions):
    up = 0
    down = 0
    position = []
    for idx, dir in enumerate(directions):
        if dir == "(":
            up += 1
        else:
            down += 1
        if up - down < 0:
            position.append(idx + 1)
    return up - down, position[0]


p1, p2 = positions(directions)
print("part1 : {}".format(p1))
print("part2 : {}".format(p2))