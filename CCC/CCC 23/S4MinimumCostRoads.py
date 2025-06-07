import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
es = []

for i in range(m):
    u, v, l, c = map(int, input().strip().split())
    es.append((u, v, l, c))

es = sorted(es, key=lambda x: x[3], reverse=True)
cc = sum(list(zip(*es))[3])
adj = [ [] for x in range(n + 1) ]
for i in es:
    adj[i[0]].append((i[1], i[2]))
    adj[i[1]].append((i[0], i[2]))

for i in es:
    (u, v, l, c) = i
    nes = es[1:]
    pq = []
    ds = [9999999999] * (n + 1)
    ds[u] = 0
    pq.append((u, 0))
    while pq:
        t = pq.pop()
        for j in adj[t[0]]:
            if ds[j[0]] > ds[t[0]] + j[1]:
                ds[j[0]] = ds[t[0]] + j[1]
                pq.append((j[0], ds[j[0]]))
        pq = sorted(pq, key=lambda x: x[1], reverse=True)
    if l >= ds[v]:
        cc -= c
        es.remove((u, v, l, c))
        if (u, l) in adj[u]:
            adj[u].remove((u, l))
        if (v, l) in adj[v]:
            adj[v].remove((v, l))

print(cc)