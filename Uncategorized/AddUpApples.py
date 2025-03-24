n = int(input())
counter = 0

def recurse(nums, total):
    count = 0
    if sum(nums) == total:
        nums = map(str, nums)
        print(str(total) + "=" + "+".join(nums))
        return 1
    else:
        for i in range(nums[-1], total - sum(nums) + 1):
            nums.append(i)
            count += recurse(nums, total)
            nums.pop()
        return count


for i in range(1, n // 2 + 1):
    counter += recurse([i], n)

print("total=" + str(counter))
