n = int(input())
e = [[False] * n for x in range(n)]
r = []
c = [0]

def place(q):
    qq = q.copy()
    for i in e:
        print(i)
    print(q)
    if len(q) == n:
        c[0] += 1
    elif frozenset(qq) not in r and e != [ [True] * n for x in range(n) ]:
        r.append(frozenset(qq))
        for k in range(n):
            for l in range(n):
                if not e[k][l]:
                    i = (k, l)
                    qq.add((k, l))
                    p = {(k, l)}
                    for j in range(n):
                        if not e[j][i[1]]:
                            p.add((j, i[1]))
                            e[j][i[1]] = True
                        if not e[i[0]][j]:
                            p.add((i[0], j))
                            e[i[0]][j] = True
                    for j in range(1, n + 1):
                        for jj in [(j, j), (j, -j), (-j, -j), (-j, j)]:
                            if 0 <= i[0] + jj[0] < n and 0 <= i[1] + jj[1] < n and not e[i[0] + jj[0]][i[1] + jj[1]]:
                                e[i[0] + jj[0]][i[1] + jj[1]] = True
                                p.add((i[0] + jj[0], i[1] + jj[1]))
                    print("___________________")
                    place(qq)
                    qq.remove((k, l))
                    for ii in p:
                        e[ii[0]][ii[1]] = False

place(set())
print(c[0])
