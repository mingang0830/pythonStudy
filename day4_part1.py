file_path = "/venvs/adventofcode_4.txt"
with open(file_path) as f:
    line = f.read().splitlines()
print(line)

data = [['hcl:5d90f0 cid:270 ecl:#66dc9c hgt:62cm byr:1945 pid:63201172 eyr:2026',],
        ['ecl:amb byr:1943 iyr:2014 eyr:2028', 'pid:333051831',],
       ]

# passports = []
#
#
# for i in line:
#     if "\n" in i:
#         i = i.replace("\n", " ")
#     passports.append(i)
#
# count = 0
#
# print(passports)
#
#
# print(count)