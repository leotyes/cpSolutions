n = int(input())
cs = {"Buttercup": set(), "Bessie": set(), "Belinda": set(), "Beatrice": set(), "Bella": set(), "Blue": set(), "Betsy": set(), "Sue": set()}
ps = []
fail = False
p = []

for i in range(n):
    x, y = input().split(" must be milked beside ")
    cs[x].add(y)
    cs[y].add(x)

def milk(l, r):
    if r == []:
        ps.append(l)
    else:
        for i in r:
            ll = l.copy()
            ll.append(i)
            rr = r.copy()
            rr.remove(i)
            milk(ll, rr)

milk([], list(cs.keys()))

for i in ps:
    fail = False
    for k, v in enumerate(i):
        if len(cs[v]) == 1:
            if k == 0:
                if i[k + 1] != list(cs[v])[0]:
                    fail = True
            elif k == len(i) - 1:
                if i[k - 1] != list(cs[v])[0]:
                    fail = True
            else:
                if i[k + 1] != list(cs[v])[0] and i[k - 1] != list(cs[v])[0]:
                    fail = True
        elif len(cs[v]) == 2:
            if k == 0:
                fail = True
            elif k == len(i) - 1:
                fail = True
            else:
                if i[k + 1] != list(cs[v])[0] or i[k - 1] != list(cs[v])[1]:
                    if i[k + 1] != list(cs[v])[1] or i[k - 1] != list(cs[v])[0]:
                        fail = True
        if fail:
            break
    if not fail:
        p.append(i)

for i in sorted(p)[0]:
    print(i)