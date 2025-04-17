n, m = map(int, input().split())
r = [ set([]) for x in range(n) ]
c = [n + 1]
con1 = con2 = True

for i in range(m):
    inp = list(map(int, input().split()))
    r[inp[0] - 1].add(inp[1])
    r[inp[1] - 1].add(inp[0])

def pizza(i, ex):
    for j in range(i + 1, n + 1):
        if j not in list(ex):
            c[0] += 1
            nl = r[j - 1].union(ex)
            pizza(j, nl)

for k, v in enumerate(r):
    pizza(k + 1, v)

print(c[0])