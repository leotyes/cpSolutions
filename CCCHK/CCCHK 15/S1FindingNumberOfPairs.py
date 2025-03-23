import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
l = 0
r = len(a) - 1
pairs = 0

while l < r:
    if a[l] + a[r] <= m:
        pairs += r - l
        l += 1
    else:
        r -= 1

print(int(min(pairs, pairs % (1e9 + 7))))