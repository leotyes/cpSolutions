w = input()
r = int(input())
c = int(input())
g = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
cc = [0]

for i in range(r):
    g.append(input().split())

def search(cw, u, cd, cl, ci):
    if cw == w:
        cc[0] += 1
    elif len(cw) < len(w) and g[cl[0]][cl[1]] == w[ci]:
        if 0 <= cl[0] + cd[0] < r and 0 <= cl[1] + cd[1] < c:
            search(cw + g[cl[0] + cd[0]][cl[1] + cd[1]], u, cd, (cl[0] + cd[0], cl[1] + cd[1]), ci + 1)
        if not u and cw != w[0]:
            t = [(cd[1], -cd[0]), (-cd[1], cd[0])]
            if 0 <= cl[0] + t[0][0] < r and 0 <= cl[1] + t[0][1] < c:
                search(cw + g[cl[0] + t[0][0]][cl[1] + t[0][1]], True, t[0], (cl[0] + t[0][0], cl[1] + t[0][1]), ci + 1)
            if 0 <= cl[0] + t[1][0] < r and 0 <= cl[1] + t[1][1] < c:
                search(cw + g[cl[0] + t[1][0]][cl[1] + t[1][1]], True, t[1], (cl[0] + t[1][0], cl[1] + t[1][1]), ci + 1)

for ki, vi in enumerate(g):
    for kj, vj in enumerate(vi):
        if vj == w[0]:
            for dr, dc in d:
                search(w[0], False, (dr, dc), (ki, kj), 0)

print(cc[0])