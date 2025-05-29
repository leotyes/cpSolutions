import sys
input = sys.stdin.readline

n, q, h = map(int, input().strip().split())
ns = []
cs = []
m = -1
psa = [0] * (n + 1)

for i in range(n):
    a, b = map(int, input().strip().split())
    ns.append([a, b])
    if a <= h:
        cs.append(True)
    else:
        cs.append(False)
    if len(psa) == 0:
        if cs[-1]:
            psa.append(b)
        else:
            psa.append(0)
    else:
        if cs[-1]:
            psa.append(b + psa[-1])
        else:
            psa.append(psa[-1])

for i in range(q):
    l, r = map(int, input().strip().split())
    if l - 2 < 0:
        if psa[r - 1] > m:
            m = psa[r - 1]
    else:
        if psa[r - 1] - psa[l - 2] > m:
            m = psa[r - 1] - psa[l - 2]

print(m)