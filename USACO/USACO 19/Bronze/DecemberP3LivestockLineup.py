from itertools import permutations

n = int(input())
cs = {"Buttercup": set(), "Bessie": set(), "Belinda": set(), "Beatrice": set(), "Bella": set(), "Blue": set(), "Betsy": set(), "Sue": set()}
ps = list(permutations(list(cs.keys())))
fail = False
p = []

for i in range(n):
    x, y = input().split(" must be milked beside ")
    cs[x].add(y)
    cs[y].add(x)

for i in ps:
    fail = False
    l = list(i)
    for k, v in enumerate(l):
        if len(cs[v]) == 1:
            if k == 0:
                if l[k + 1] != list(cs[v])[0]:
                    fail = True
            elif k == len(l) - 1:
                if l[k - 1] != list(cs[v])[0]:
                    fail = True
            else:
                if l[k + 1] != list(cs[v])[0] and l[k - 1] != list(cs[v])[0]:
                    fail = True
        elif len(cs[v]) == 2:
            if k == 0:
                fail = True
            elif k == len(l) - 1:
                fail = True
            else:
                if l[k + 1] != list(cs[v])[0] or l[k - 1] != list(cs[v])[1]:
                    if l[k + 1] != list(cs[v])[1] or l[k - 1] != list(cs[v])[0]:
                        fail = True
        if fail:
            break
    if not fail:
        p.append(l)

for i in sorted(p)[0]:
    print(i)