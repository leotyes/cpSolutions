x = int(input())
y = int(input())
s = 0
sp = [0, 0]
dc = 1
d = 0
cp = []
cn = x + 1
bb = False
if (y - x + 1) ** .5 // 1 == (y - x + 1) ** .5:
    s = int((y - x + 1) ** .5)
else:
    s = int((((y - x + 1) ** .5) // 1) + 1)
g = [ [""] * s for x in range(s) ]

if s % 2 == 1:
    sp = [s // 2, s // 2]
else:
    sp = [s // 2 - 1, s // 2 - 1]
cp = sp[:]
g[sp[0]][sp[1]] = x
for i in range(x + 1, y + 1):
    if d == 0:
        for j in range(1, dc + 1):
            if cn != y + 1:
                g[cp[0] + j][cp[1]] = cn
                cn += 1
            else:
                bb = True
                break
        cp = [cp[0] + dc, cp[1]]
        d += 1
    elif d == 1:
        for j in range(1, dc + 1):
            if cn != y + 1:
                g[cp[0]][cp[1] + j] = cn
                cn += 1
            else:
                bb = True
                break
        cp = [cp[0], cp[1] + dc]
        d += 1
        dc += 1
    elif d == 2:
        for j in range(1, dc + 1):
            if cn != y + 1:
                g[cp[0] - j][cp[1]] = cn
                cn += 1
            else:
                bb = True
                break
        cp = [cp[0] - j, cp[1]]
        d += 1
    elif d == 3:
        for j in range(1, dc + 1):
            if cn != y + 1:
                g[cp[0]][cp[1] - j] = cn
                cn += 1
            else:
                bb = True
                break
        cp = [cp[0], cp[1] - j]
        d = 0
        dc += 1
    if bb:
        break

for i in g:
    print(*i)