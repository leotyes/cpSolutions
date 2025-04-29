import sys
input = sys.stdin.readline

n, q = map(int, input().strip().split())
c = list(map(int, input().strip().split()))
t = list(map(int, input().strip().split()))
ct = sorted([ a - b for a, b in zip(c, t) ], reverse=True)
cc = 0

for i in range(q):
    cc = 0
    v, s = map(int, input().strip().split())
    if ct[v - 1] > s:
        print("YES")
    else:
        print("NO")