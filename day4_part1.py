file_path = "/venvs/adventofcode_4.txt"
with open(file_path) as f:
    line = f.read()

line = line.split("\n\n")
passports = []


for i in line:
    if "\n" in i:
        i = i.replace("\n", " ")
    passports.append(i)

count = 0

for i in passports:
    if "byr" and "iyr" and "eyr" and "hgt" and "hcl" and "ecl" and "pid" in i:
        count += 1


print(count)