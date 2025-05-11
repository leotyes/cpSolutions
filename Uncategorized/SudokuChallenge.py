s = []
sf = []

for i in range(9):
    s.append(list(input()))
sf = [ list(x) for x in list(zip(*s)) ]

def solve(cs, csf, cl, ah, asq):
    a = []
    ahn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    avn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    asqn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chsq = False
    chh = False
    p = False
    if cs[cl[0]][cl[1]] == ".":
        p = True
        for i in csf[cl[1]]:
            if i != ".":
                avn.remove(int(i))
    if cl[1] % 3 == 0:
        chsq = True
        if cl[1] == 0:
            chh = True
            for i in cs[cl[0]]:
                if i != ".":
                    ahn.remove(int(i))
        for i in range(cl[0] - (cl[0] % 3), cl[0] - (cl[0] % 3) + 3):
            for j in range(cl[1], cl[1] + 3):
                if cs[i][j] != "." and int(cs[i][j]) in asqn:
                    asqn.remove(int(cs[i][j]))
    if not chh:
        ahn = ah
    if not chsq:
        asqn = asq
    for i in avn:
        if i in ahn and i in asqn:
            a.append(i)
    if not p:
        csc = [ x[:] for x in cs ]
        if cl[1] == 8:
            if cl[0] != 8:
                r = solve(csc, [ list(x) for x in list(zip(*csc)) ], [cl[0] + 1, 0], [], [])
                if r: return r
            else:
                return csc
        else:
            r = solve(csc, [ list(x) for x in list(zip(*csc)) ], [cl[0], cl[1] + 1], ahn[:], asqn[:])
            if r: return r
    else:
        for i in a:
            csc = [ x[:] for x in cs ]
            csc[cl[0]][cl[1]] = str(i)
            if cl[1] == 8:
                if cl[0] != 8:
                    r = solve(csc, [ list(x) for x in list(zip(*csc)) ], [cl[0] + 1, 0], [], [])
                    if r: return r
                else:
                    return csc
            else:
                ahnn = ahn[:]
                ahnn.remove(i)
                asqnn = asqn[:]
                asqnn.remove(i)
                r = solve(csc, [ list(x) for x in list(zip(*csc)) ], [cl[0], cl[1] + 1], ahnn[:], asqnn[:])
                if r: return r

r = solve(s[:], sf, [0, 0], [], [])

for i in r:
    print("".join(i))