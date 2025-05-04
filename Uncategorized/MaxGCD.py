n = int(input())
ns = list(map(int, input().split()))
p = []
s = []
m = 0
o = 0

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if n == 2:
    print(max(ns))
else:
    p.append(ns[0])
    o = gcd(ns[0], ns[1])
    p.append(o)

    for i in range(1, n - 1):
        o = gcd(o, ns[i + 1])
        p.append(o)

    s.append(ns[-1])
    o = gcd(ns[-1], ns[-2])
    s.append(o)

    for i in range(n - 2, 0, -1):
        o = gcd(o, ns[i - 1])
        s.append(o)

    m = p[-2]
    m = max(s[-2], m)

    for i in range(1, n - 1):
        m = max(m, gcd(p[i - 1], s[-2 - i]))

    print(m)