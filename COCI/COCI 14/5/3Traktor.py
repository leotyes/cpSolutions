import sys
input = sys.stdin.readline

n, k = map(int, input().split())
r = [0] * (10 ** 5)
c = [0] * (10 ** 5)
ld = [0] * (((10 ** 5) * 2) - 1)
rd = [0] * (((10 ** 5) * 2) - 1)
a = -1

for i in range(1, n + 1):
    x, y = map(int, input().split())
    r[x] += 1
    if r[x] == k:
        a = i
        break
    c[y] += 1
    if c[y] == k:
        a = i
        break
    rd[x - y + (10 ** 5) - 1] += 1
    if rd[x - y + (10 ** 5) - 1] == k:
        a = i
        break
    ld[x + y] += 1
    if ld[x + y] == k:
        a = i
        break

print(a)