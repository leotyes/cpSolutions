n, m = map(int, input().split())
q = []
p = set()

for i in range(m):
    q.append(tuple(map(int, input().split())))

for i in q:
    s1 = s2 = s3 = s4 = False
    for j in range(1, n + 1):
        p.add(tuple([j, i[1]]))
    for j in range(1, n + 1):
        p.add(tuple([i[0], j]))
    for j in range(1, n + 1):
        c = False
        if i[0] + j <= n and i[1] + j <= n and not s1:
            if tuple([i[0] + j, i[1] + j]) in q:
                s1 = True
            c = True
            p.add(tuple([i[0] + j, i[1] + j]))
        if i[0] + j <= n and i[1] - j > 0 and not s2:
            if tuple([i[0] + j, i[1] - j]) in q:
                s2 = True
            c = True
            p.add(tuple([i[0] + j, i[1] - j]))
        if i[0] - j > 0 and i[1] - j > 0 and not s3:
            if tuple([i[0] - j, i[1] - j]) in q:
                s3 = True
            c = True
            p.add(tuple([i[0] - j, i[1] - j]))
        if i[0] - j > 0 and i[1] + j <= n and not s4:
            if tuple([i[0] - j, i[1] + j]) in q:
                s4 = True
            c = True
            p.add(tuple([i[0] - j, i[1] + j]))
        if not c:
            break

print(n * n - len(p))