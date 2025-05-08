n, k = map(int, input().split())
ns = sorted(list(map(int, input().split())))
d = []
c = k + 1

for kk, v in enumerate(ns):
    if kk != len(ns) - 1:
        d.append(ns[kk + 1] - v)

for i in d:
    if i < k + 1:
        c += i
    else:
        c += k + 1

print(c)