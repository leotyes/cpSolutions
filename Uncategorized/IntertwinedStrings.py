from functools import cache

s, t = input().split()
memo = []

@cache
def construct(l, sc, tc):
    if sc != len(s):
        construct(l + s[sc], sc + 1, tc)
    if tc != len(t):
        construct(l + t[tc], sc, tc + 1)
    if tc == len(t) and sc == len(s):
        print(l)

construct("", 0, 0)

# maybe make my own memoization