file_path = "2018_day3.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


def parse(puzzle):
    claims = []
    for data in puzzle:
        id = int(data.split(" ")[0][1:])
        x, y = int(data.split(" ")[2].split(",")[0]), int(data.split(" ")[2].split(",")[1][:-1])
        wide, tall = int(data.split(" ")[3].split("x")[0]), int(data.split(" ")[3].split("x")[1])
        claims.append({"id": id, "x": x, "y": y, "wide": wide, "tall": tall})
    return claims


claims = parse(puzzle)

id_and_inches = {}
inches_of_id = []
all_inches = []
for claim in claims:
    for w in range(claim["wide"]):
        for t in range(claim["tall"]):
            all_inches.append((claim["x"] + w, claim["y"] + t))
            inches_of_id.append((claim["x"] + w, claim["y"] + t))
    id_and_inches[claim["id"]] = inches_of_id
    inches_of_id = []

result = {}

for inch in all_inches:
    if inch not in result:
        result[inch] = 1
    else:
        result[inch] += 1

count = 0
not_overlap = []
for k, v in result.items():
    if v >= 2:
        count += 1
    elif v == 1:
        not_overlap.append(k)

print("part1 : {}".format(count))

set_not_overlap = set(not_overlap)

for k, v in id_and_inches.items():
    set_v = set(v)
    if set_v - set_not_overlap == set():
        print("part2 : {}".format(k))


