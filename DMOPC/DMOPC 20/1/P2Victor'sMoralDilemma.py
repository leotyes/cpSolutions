n, d = map(int, input().split())
a = list(map(int, input().strip().split()))
for i in range(d):
    ni = int(input())
    if sum(a[:ni]) >= sum(a[ni:]):
        print(sum(a[:ni]))
        a = a[ni:]
    else:
        print(sum(a[ni:]))
        a = a[:ni]