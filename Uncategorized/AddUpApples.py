n = int(input())
dp = []

# recursion way
# def appleWays(apples: int):
#     if apples == 1:
#         return [[1]]
#     else:
#         return appleWays(apples - 1) + 1
# appleWays(n)

dp.append([[1]])