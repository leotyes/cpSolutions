n = int(input())
ns = list(map(int, input().split()))
m = 0
o = 0

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

for k, v in enumerate(ns):
    new = ns[:]
    del new[k]
    o = gcd(new[0], new[1])
    for i in range(1, len(new) - 1):
        o = gcd(o, new[i + 1])
    m = max(m, o)

print(m)