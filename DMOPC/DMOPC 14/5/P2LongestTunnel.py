import sys
input = sys.stdin.readline

n = int(input())
m = 0

for i in range(n):
    x1, x2 = map(int, input().strip().split())
    d = abs(x1 - x2)
    m = max(m, d)

print(m)