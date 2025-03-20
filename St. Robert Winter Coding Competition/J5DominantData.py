n = int(input())
d = {}
keys = []
found = False

for i in range(n):
    j = int(input())
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

keys = sorted(d.keys(), reverse=True)

for i in keys:
    if d[i] >= n // 2:
        print(i)
        found = True
        break

if found is False:
    print("-1")