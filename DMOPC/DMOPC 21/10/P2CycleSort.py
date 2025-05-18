import sys

n = int(input())
ns = list(map(int, input().split()))
ns = ns[ns.index(1):] + ns[:ns.index(1)]

if ns == sorted(ns):
    print(*ns)
    sys.exit()

for k, v in enumerate(ns):
    if k + 1 != v:
        if ns[1] == 2:
            ni = ns.index(k + 1)
            ns[k], ns[ni] = ns[ni], ns[k]
            print(*ns)
            break
        else:
            a = ns[:]
            b = ns[:]
            c = ns[:]
            ti = ns.index(2)
            a[1], a[ti] = a[ti], a[1]
            b[0], b[ti - 1] = b[ti - 1], b[0]
            c[0], c[ti] = c[ti], c[0]
            b = b[b.index(1):] + b[:b.index(1)]
            c = c[c.index(1):] + c[:c.index(1)]
            print(*min(a, b, c))
            break