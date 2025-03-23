import math

a = int(input())
b = int(input())
answers = []
nums = [ False for x in range(b + 1) ]
answers = [ 0 for x in range(b - a + 1) ]
nums[0] = True
nums[1] = True

for j in range(2, b):
    if not nums[j]:
        for k in range(2 * j, b + 1, j):
            nums[k] = True
            if k >= a:
                answers[k - a] += 1

for i in answers:
    if i == 0:
        print(1)
    else:
        print(i)