n, l = map(int, input().split())
ss = []

def search(p, i):
    print(str(p))
    if len(p) != l:
        for z in range(i + 1, len(ss)):
            for y in ss[z]:
                search(p + y, z)

for i in range(n):
    s = input().split()
    m = s[0]
    del s[0]
    ss.append(s)

for j in ss[0]:
    search(j, 0)