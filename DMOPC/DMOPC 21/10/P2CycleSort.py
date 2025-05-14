n = int(input())
ns = list(map(int, input().split()))
i = 0

for k, v in enumerate(reversed(ns)):
    if k + 1 != v:
        ns[ns.index(k + 1)], ns[-(k + 1)] = ns[-(k + 1)], ns[ns.index(k + 1)]
        i = -(k + 1)
        break

ns = [ str(x) for x in ns]
print(" ".join(ns[i:][::-1]) + " " + " ".join(ns[:i]))