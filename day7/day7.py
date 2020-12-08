import re

bags = {}
# with open('test.txt') as f:
with open('input.txt') as f:
    lines = [l for l in f.read().split("\n") if len(l) != 0]

first_bag = re.compile("\\w+ \\w+ bag")
rest_bags = re.compile("\\d \\w+ \\w+ bag")


def parse_bag(bag: str) -> (str, {str, int}):
    first = first_bag.match(bag).group()
    rest = {}

    for b in rest_bags.findall(bag):
        tokens = b.split(" ")
        rest[" ".join(tokens[1:])] = int(tokens[0])

    return (first, rest)


bags = []
for l in lines:
    bags.append(parse_bag(l))

bags = dict(bags)


def find_shiny(bagsToSearch: [str]) -> bool:
    for b in bagsToSearch:
        if "shiny gold" in b:
            return True

        if find_shiny([k for k in bags[b]]):
            return True

    return False


count = 0
for key in bags:
    if find_shiny([k for k in bags[key]]):
        count += 1

print(f"PART 1: {count}")


def calc_bags(bagToSearch: str) -> bool:
    calc = 0
    inner = bags[bagToSearch]
    for key in inner:
        calc += calc_bags(key) * inner[key] + inner[key]

    return calc


count = 0
for key in bags["shiny gold bag"]:
    count += calc_bags(key) + 1

print(f"PART 2: {count}")
