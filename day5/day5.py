with open('input.txt') as f:
    lines = f.read().split("\n")


def get_row(s: str) -> int:
    lower = 0
    upper = 127
    for _, row in enumerate(s[0:7]):
        if row == "F":
            upper = (upper + lower) // 2
        elif row == "B":
            lower = lower + (upper - lower + 1) // 2

    return lower


def get_column(s: str) -> int:
    lower = 0
    upper = 7
    for _, row in enumerate(s[7:10]):
        if row == "L":
            upper = (upper + lower) // 2
        elif row == "R":
            lower = lower + (upper - lower + 1) // 2

    return lower


ids = []
max_id = 0
for p in lines:
    seat_id = get_row(p) * 8 + get_column(p)
    max_id = max(max_id, seat_id)
    ids.append(seat_id)

print(f"PART 1: {max_id}")

ids.sort()
for i, seat_id in enumerate(range(ids[8], ids[-8])):
    if ids[i+8] != seat_id:
        print(seat_id)
        break
