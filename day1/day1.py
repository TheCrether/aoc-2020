with open('input.txt') as f:
    lines = f.read().split("\n")
    nums = []
    for l in lines:
        if len(l) == 0:
            continue
        nums.append(int(l))


def part1():
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


def part2():
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]


print(f"[+] PART 1: {part1()}")
print(f"[+] PART 2: {part2()}")
