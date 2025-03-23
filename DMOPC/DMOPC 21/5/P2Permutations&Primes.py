# # just find one pair of even and odd numbers that is not a prime and you are done
# import math
#
# n = int(input())
# pmax = 2 * n - 1
# nums = [ False for x in range(pmax + 1) ]
# nums[0] = True
# nums[1] = True
# nums[2] = True
#
# for j in range(3, int((math.sqrt(pmax) // 1) + 1)):
#     if not nums[j]:
#         for k in range(2 * j, pmax + 1, j):
#             nums[k] = True
#
# for k, v in enumerate(nums):
#     if v and k % 2 == 1:
#         for i in range(1, n, 2)