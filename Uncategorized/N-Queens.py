n = int(input())
e = [[False] * n for x in range(n)]
r = []
c = [0]


def place(q):
    ex = []
    qq = q.copy()
    if e == [[True] * n for x in range(n)]:
        c[0] += 1
    elif not q in r:
        for k, v in enumerate(e):
            for l, m in enumerate(v):
                if m:
                    ex.append([k + 1, l + 1])
        for k, v in enumerate(e):
            for l, m in enumerate(v):
                if not m:
                    i = (k, l)
                    qq.add((k, l))
                    r.append(qq)
                    p = set()
                    for j in range(n):
                        p.add(tuple([j, i[1]]))
                    for j in range(n):
                        p.add(tuple([i[0], j]))
                    for j in range(n):
                        if i[0] + j < n and i[1] + j < n:
                            e[i[0] + j][i[1] + j] = True
                            p.add(tuple([i[0] + j, i[1] + j]))
                        if i[0] + j < n and i[1] - j >= 0:
                            e[i[0] + j][i[1] - j] = True
                            p.add(tuple([i[0] + j, i[1] - j]))
                        if i[0] - j >= 0 and i[1] - j >= 0:
                            e[i[0] - j][i[1] - j] = True
                            p.add(tuple([i[0] - j, i[1] - j]))
                        if i[0] - j >= 0 and i[1] + j < n:
                            e[i[0] - j][i[1] + j] = True
                            p.add(tuple([i[0] - j, i[1] + j]))
                    place(qq)
                    for ii in p:
                        if ii not in ex:
                            e[i[0]][i[1]] = False

place(set())
print(c[0])
