file_path = "2015_day2.txt"
with open(file_path) as f:
    puzzle = f.read().splitlines()

data = []
for ele in puzzle:
    l_w_h = ele.split("x")
    length = int(l_w_h[0])
    width = int(l_w_h[1])
    height = int(l_w_h[2])

    data.append({"length": length,
                 "width": width,
                 "height": height})

wrapping_papers = 0
ribbon = 0
for ele in data:
    l = ele["length"]
    w = ele["width"]
    h = ele["height"]
    surface_area = 2 * (l*w + w*h + h*l)
    extra_paper = min(l*w, w*h, h*l)
    shortest_side = min(l+w, w+h, l+h)

    wrapping_papers += surface_area + extra_paper
    ribbon += shortest_side * 2 + (l*w*h)

print("part1 : {}".format(wrapping_papers))
print("part2 : {}".format(ribbon))


