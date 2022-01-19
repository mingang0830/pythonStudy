import re
from collections import defaultdict

file_path = "2018_day3.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()


def parse(puzzle):
    """
    docstring == document string
    함수의 설명
    parse 는 puzzle 을 입력받아
    id,x,y,wide,tall 을 키로 하는 dict를 반환합니다.

    example: 입력받는 puzzle의 예제
    #1 @ 387,801: 11x22
    ...
    """
    claims = []
    for line in puzzle:
        id_, x, y, width, height = map(int, re.findall(r"^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$", line)[0])
        claims.append({
            "id": id_,
            "x": x,
            "y": y,
            "wide": width,
            "tall": height})
    return claims


claims = parse(puzzle)


def make_square(x, y, width, height):
    result = []
    for w in range(width):
        for h in range(height):
            result.append((x + w, y + h))
    return result


id_and_inches = {}
for claim in claims:
    id_and_inches[claim["id"]] = make_square(claim["x"], claim["y"], claim["wide"], claim["tall"])
    # id_and_inches = {1: [(0, 0), (0, 1), (1, 0), (1, 1)], 2: ..., ...}


def inch_count(data):
    result = defaultdict(int)
    for coords in data:
        for coord in coords:
            result[coord] += 1
    return result


result = inch_count(id_and_inches.values())
# result = {(0,0): 1, (0,1): 1, ... (3,3): 3, ...}

part1_answer = 0
for coord, count in result.items():  # 1차원의 고정된 loop == O(n)
    if count > 1:
        part1_answer += 1

not_overlapped = set()
for coord, count in result.items():  # 1차원의 고정된 loop == O(n)
    if count == 1:
        not_overlapped.add(coord)
# O(n) + O(n) != 2O(n)
# O(n) + O(n) = O(n)
# 가독성을 챙기는게 낫다.

print("part1 : {}".format(part1_answer))

for id_, coords in id_and_inches.items():
    if not set(coords) - not_overlapped:
        print("part2 : {}".format(id_))
