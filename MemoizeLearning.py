from functools import cache
memo = [0] * 999999999
# @cache lazy way
def fib(n):
    if n <= 1:
        return n
    if memo[n]:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

for i in range(999999999):
    print(fib(i))