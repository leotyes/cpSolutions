n, s = map(int, input().split())
a = list(map(int, input().split()))
da = {v: k for k, v in enumerate(a)}
sa = sorted(a, reverse=True)
c = 0

for k, v in enumerate(a):
    if v != sa[k]:
        c += 1
        i = da[sa[k]]
        da[sa[k]], da[v] = da[v], da[sa[k]]
        a[k], a[i] = a[i], a[k]
    if c == s:
        break

a = [ str(x) for x in a ]
print(" ".join(a))