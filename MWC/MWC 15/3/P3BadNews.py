import sys
input = sys.stdin.readline

n, q = map(int, input().strip().split())
c = []
w = []
d = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

for i in range(n):
    c.append(input().strip().split())

for i in range(q):
    w.append(input().strip())

wr = [False] * len(w)

def search(cp, cw, nw, u):
    if cw == w[nw]:
        wr[nw] = True
    else:
        for i in d:
            np = [cp[0] + i[0], cp[1] + i[1]]
            if 0 <= np[0] < n and 0 <= np[1] < n:
                if c[np[0]][np[1]] == w[nw][len(cw)]:
                    if [np[0], np[1]] not in u:
                        uu = u[:]
                        uu.append(np)
                        search(np, cw + c[np[0]][np[1]], nw, uu)

for ki, vi in enumerate(c):
    for kj, vj in enumerate(vi):
        for k in range(len(w)):
            if vj == w[k][0]:
                search([ki, kj], vj, k, [[ki, kj]])

for i in wr:
    if i:
        print("good puzzle!")
    else:
        print("bad puzzle!")