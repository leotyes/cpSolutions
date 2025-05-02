n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
f = [0] * (n + 1)
r = [ x for x in range(1, n + 1) ]
p1 = 0
p2 = 0

f[1] = 1
for i in range(2, len(f)):
    f[i] = i * f[i - 1]

for k, v in enumerate(p):
    i = r.index(v)
    r.remove(v)
    p1 += i * f[n - k - 1]

r = [ x for x in range(1, n + 1) ]
for k, v in enumerate(q):
    i = r.index(v)
    r.remove(v)
    p2 += i * f[n - k - 1]

print(abs(p1 - p2))