file_path = "2021_day2.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


def command_split(command):
    cur_command = command.split(" ")
    dir_ = cur_command[0]
    units = int(cur_command[1])
    return dir_, units


horizon = 0
depth = 0
for command in puzzle:
    dir_, units = command_split(command)
    if dir_ == "forward":
        horizon += units
    elif dir_ == "down":
        depth += units
    elif dir_ == "up":
        depth -= units

print("part1 : {}".format(horizon * depth))

horizon = 0
depth = 0
aim = 0
for command in puzzle:
    dir_, units = command_split(command)
    if dir_ == "forward":
        horizon += units
        depth += units * aim
    elif dir_ == "down":
        aim += units
    elif dir_ == "up":
        aim -= units

print("part2 : {}".format(horizon * depth))
