with open("input.txt") as f:
    groups = f.read().split("\n\n")

count = 0
for group in groups:
    answered = []
    for _, ans in enumerate(group.replace("\n", "")):
        if ans not in answered:
            answered.append(ans)

    count += len(answered)

print(f"PART 1: {count}")

count = 0
for group in groups:
    answered = {}
    for _, ans in enumerate(group.replace("\n", "")):
        if ans not in answered:
            answered[ans] = 1
        else:
            answered[ans] += 1

    l = len([g for g in group.split("\n") if len(g.strip()) != 0])
    for key in answered:
        if l == answered[key]:
            count += 1

print(f"PART 2: {count}")
