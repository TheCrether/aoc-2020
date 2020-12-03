def countTrees(lines: [str], x: int, y: int) -> int:
    trees = 0
    actual_x = x
    actual_y = y
    l = len(lines[0])
    while True:
        if actual_y >= len(lines) or len(lines[actual_y]) == 0:
            break
        tree = lines[actual_y][actual_x % l]
        if tree == "#":
            trees += 1

        actual_x += x
        actual_y += y

    return trees


with open('input.txt') as f:
    lines = f.read().split("\n")

part1 = countTrees(lines, 3, 1)
print(f"PART 1: {part1}")

# Part 2
no1 = countTrees(lines, 1, 1)
no2 = part1
no3 = countTrees(lines, 5, 1)
no4 = countTrees(lines, 7, 1)
no5 = countTrees(lines, 1, 2)

print(f"PART 2: {no1 * no2 * no3 * no4 * no5}")
