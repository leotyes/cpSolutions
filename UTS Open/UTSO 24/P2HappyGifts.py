import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
ns = list(map(int, input().strip().split()))
ck = -1
m = 0
pns = []
nns = []
for i in ns:
    if i > 0:
        pns.append(i)
    elif i < 0:
        nns.append(i)
pns = sorted(pns, reverse=True)[:k]
nns = sorted(nns, reverse=True)
ck = len(pns)
m = sum(pns)
while ck > 0:
    if len(pns) == 0:
        ck -= 2
        if ck <= 0:
            break
        else:
            m = max(m, m - nns.pop())
    else:
        ck -= 1
        if ck == 0:
            break
        else:
            m = max(m, m - pns.pop() - nns.pop())

print(m)