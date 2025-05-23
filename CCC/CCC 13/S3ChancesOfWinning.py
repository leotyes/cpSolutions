t = int(input())
g = int(input())
p = [0, 0, 0, 0]
u = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
cc = [0]

for i in range(g):
    a, b, sa, sb = map(int, input().split())
    aa = a - 1
    bb = b - 1
    u.remove([aa, bb])
    if sa > sb:
        p[aa] = p[aa] + 3
    elif sa == sb:
        p[aa] = p[aa] + 1
        p[bb] = p[bb] + 1
    else:
        p[bb] = p[bb] + 3

def play(rg, cp):
    if len(rg) == 0:
        if max(cp) == cp[t - 1] and cp.count(max(cp)) == 1:
            cc[0] += 1
    else:
        ccp = cp[:]
        rrg = rg[:]
        ccp[rg[0][0]] += 3
        rrg.remove(rrg[0])
        play(rrg, ccp)
        ccp = cp[:]
        rrg = rg[:]
        ccp[rg[0][1]] += 3
        rrg.remove(rrg[0])
        play(rrg, ccp)
        ccp = cp[:]
        rrg = rg[:]
        ccp[rg[0][0]] += 1
        ccp[rg[0][1]] += 1
        rrg.remove(rrg[0])
        play(rrg, ccp)

play(u, p)
print(cc[0])