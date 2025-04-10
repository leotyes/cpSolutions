n = list(input())
a = []

def construct(s, r):
    if len(s) == len(n):
        a.append(s)
    else:
        for i in r:
            x = r[:]
            x.remove(i)
            construct(s + i, x)

construct("", n)

for i in sorted(a):
    print(i)