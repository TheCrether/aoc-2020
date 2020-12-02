with open("input.txt") as f:
    lines = f.read().split("\n")

correct1 = 0
correct2 = 0

for l in lines:
    if len(l.strip(" ")) == 0:
        continue

    msplit = l.split(":")
    con = msplit[0].split(" ")
    n = con[0].split("-")
    lower, upper = int(n[0]), int(n[1])
    pw = msplit[1].strip()
    count = 0

    # part 1
    for c in pw:
        if c == con[1]:
            count += 1

    if lower <= count and count <= upper:
        correct1 += 1

    # part 2
    count = 0
    first, second = pw[lower-1] == con[1], pw[upper-1] == con[1]

    if (first and not second) or (not first and second):
        correct2 += 1

print(f"PART 1: {correct1}")
print(f"PART 2: {correct2}")
