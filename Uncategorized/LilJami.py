import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
ns = [0] * (n + 1)
for i in range(k):
    ns[int(input()) + 1] += 1
for i in range(1, len(ns)):
    ns[i] += ns[i - 1]
q = int(input())
for i in range(q):
    a, b = map(int, input().strip().split())
    print(ns[b + 1] - ns[a])