import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, s = map(int, input().strip().split())
    ts = n * (n + 1) // 2
    rs = ts - s
    l = max(1, rs - n)
    h = min(n, (rs - 1) // 2)
    print(h - l + 1)