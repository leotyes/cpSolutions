import sys
input = sys.stdin.readline

g = []
s = [ [False] * 10 for x in range(9) ]
r = [ [False] * 10 for x in range(9) ]
c = [ [False] * 10 for x in range(9) ]
e = []

for i in range(9):
    g.append(list(input().strip()))

def solve(ci):
    a = e[ci]
    if ci == len(e) - 1:
        for i in range(1, 10):
            if not r[a[0]][i] and not c[a[1]][i] and not s[(a[0] // 3 * 3 + a[1] // 3)][i]:
                g[a[0]][a[1]] = str(i)
        for i in g:
            print("".join([ int(x) if type(x) == int else x for x in i ]))
        sys.exit(0)
    else:
        for i in range(1, 10):
            if not r[a[0]][i] and not c[a[1]][i] and not s[(a[0] // 3 * 3 + a[1] // 3)][i]:
                r[a[0]][i] = True
                c[a[1]][i] = True
                s[(a[0] // 3 * 3 + a[1] // 3)][i] = True
                g[a[0]][a[1]] = str(i)
                solve(ci + 1)
                r[a[0]][i] = False
                c[a[1]][i] = False
                s[(a[0] // 3 * 3 + a[1] // 3)][i] = False

for k, v in enumerate(g):
    for l, m in enumerate(v):
        if m == ".":
            e.append([k, l])
        else:
            r[k][int(m)] = True
            c[l][int(m)] = True
            ss = k // 3 * 3 + l // 3
            s[ss][int(m)] = True

solve(0)