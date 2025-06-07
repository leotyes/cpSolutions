import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b, c, d = map(int, input().strip().split())
    if b * d > b * c + a * d:
        print("YES")
    else:
        print("NO")