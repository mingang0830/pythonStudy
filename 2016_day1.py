import re

file_path = "2016_day1.txt"
with open(file_path) as f:
    puzzle = f.read()


right_direction_map = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

left_direction_map = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N",
}


def parse(lines):
    result = []
    for direction, step in re.findall(r"([R|L]{1})([0-9]+)", lines):
        result.append((direction, int(step)))
    return result


def get_next_direction(cur_direction, faced_direction):
    if cur_direction == "R":
        return right_direction_map[faced_direction]
    elif cur_direction == "L":
        return left_direction_map[faced_direction]


def move(cur_direction, coord, step):
    if cur_direction == "N":
        coord[1] += step
    elif cur_direction == "E":
        coord[0] += step
    elif cur_direction == "S":
        coord[1] -= step
    elif cur_direction == "W":
        coord[0] -= step
    return coord


def get_distance(coord):
    return abs(coord[0]) + abs(coord[1])


def solve(line):
    cur_coord = [0, 0]
    cur_direction = "N"
    for direction, step in parse(line):
        cur_direction = get_next_direction(direction, cur_direction)
        cur_coord = move(cur_direction, cur_coord, step)
    return get_distance(cur_coord)


print("part 1 : {}".format(solve(puzzle)))
