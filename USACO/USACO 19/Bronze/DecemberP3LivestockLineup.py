n = int(input())
cs = {"Buttercup": set(), "Bessie": set(), "Belinda": set(), "Beatrice": set(), "Bella": set(), "Blue": set(), "Betsy": set(), "Sue": set()}
r = []
p = []

for i in range(n):
    x, y = input().split(" must be milked beside ")
    cs[x].add(y)
    cs[y].add(x)

def milk(l, c, r):
    ll = l.copy()
    cc = { k: v.copy() for k, v in c.items() }
    rr = r.copy()
    if len(ll) == 8:
        p.append(l)
    elif len(cc[ll[-1]]) == 0:
        for kk in rr:
            rra = rr.copy()
            lla = ll.copy()
            lla.append(kk)
            rra.remove(kk)
            milk(lla, cc, rra)
    elif len(cc[ll[-1]]) == 1:
        neigh = list(cc[ll[-1]])[0]
        if neigh in rr:
            ii = ll[-1]
            ll.append(neigh)
            rr.remove(neigh)
            cc[neigh].remove(ii)
            cc[ii].remove(neigh)
            milk(ll, cc, rr)
    else:
        neigh1 = list(cc[ll[-1]])[0]
        ll1 = ll.copy()
        i1 = ll1[-1]
        rr1 = rr.copy()
        cc1 = { k: v.copy() for k, v in cc.items() }
        ll1.append(neigh1)
        rr1.remove(neigh1)
        cc1[neigh1].remove(i1)
        cc1[i1].remove(neigh1)
        milk(ll1, cc1, rr1)
        neigh2 = list(cc[ll[-1]])[1]
        ll2 = ll.copy()
        i2 = ll2[-1]
        rr2 = rr.copy()
        cc2 = { k: v.copy() for k, v in cc.items() }
        ll2.append(neigh2)
        rr2.remove(neigh2)
        cc2[neigh2].remove(i2)
        cc2[i2].remove(neigh2)
        milk(ll2, cc2, rr2)


for i in cs.keys():
    na = list(cs.keys())
    na.remove(i)
    milk([i], cs, na)

for i in sorted(p)[0]:
    print(i)