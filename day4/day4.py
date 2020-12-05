from re import split
import re
import time

needed = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


def is_valid_passport(passport: str) -> bool:
    fields = [field.split(":")[0] for field in passport]
    return all(elem in fields for elem in needed)


with open('input.txt') as f:
    all_passports = f.read().split("\n\n")
    # split the input so that I can use it lol
    passports = [
        [field for field in split("( |\n)", passport) if field.strip() != ""]
        for passport in all_passports]

valid = 0

for passport in passports:
    if is_valid_passport(passport):
        valid += 1

print(f"PART 1: {valid}")


def byr(s: str) -> bool:
    return 1920 <= int(s) <= 2002


def iyr(s: str) -> bool:
    return 2010 <= int(s) <= 2020


def eyr(s: str) -> bool:
    return 2020 <= int(s) <= 2030


def hgt(s: str) -> bool:
    if not s.endswith("cm") and not s.endswith("in"):
        return False

    if s.endswith("cm"):
        if len(s) != 5:
            return False
        return 150 <= int(s[0:3]) <= 193

    if s.endswith("in"):
        if len(s) != 4:
            return False
        return 59 <= int(s[0:2]) <= 76

    return False


re_hcl = re.compile("#[0-9a-f]{6}")


def hcl(s: str) -> bool:
    result = re_hcl.match(s)
    return result != None


def ecl(s: str) -> bool:
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return s in colors


def pid(s: str) -> bool:
    return len(s) == 9 and s.isnumeric()


validators = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid
}

value = 0
for passport in passports:
    if not is_valid_passport(passport):
        continue

    is_valid = True

    for field in passport:
        tokens = field.split(":")
        if tokens[0] == "cid":
            continue

        if not validators[tokens[0]](tokens[1]):
            is_valid = False
            break

    print(passport)
    # input(str(is_valid))

    if is_valid:
        value += 1

print(f"PART 2: {value}")
