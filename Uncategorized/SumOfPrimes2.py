import math

q = int(input())
answers = []
q0 = []
q1 = []

for i in range(q):
    ab = [ int(x) for x in input().split(" ") ]
    q0.append(ab[0])
    q1.append(ab[1])

q1max = max(q1)
nums = [ False for x in range(q1max + 1) ]
nums[0] = True
nums[1] = True

for j in range(2, int((math.sqrt(q1max) // 1) + 1)):
    if not nums[j]:
        for k in range(2 * j, q1max + 1, j):
            nums[k] = True
# i think i need a prefix sum array
for i in range(q):
    sum1 = 0
    for j in range(q0[i], q1[i] + 1):
        if not nums[j]:
            sum1 += j
    print(sum1)