n = int(input())
ings = []
m = [1000000000]

def check(s, b, k):
    if k + 1 == n:
        m[0] = min(m[0], abs(s - b))
    else:
        for i in range(k + 1, n):
            m[0] = min(m[0], abs(s - b))
            ns = s * ings[i][0]
            nb = b + ings[i][1]
            check(ns, nb, i)

if n == 1:
    l = list(map(int, input().split()))
    print(abs(l[0] - l[1]))
else:
    for i in range(n):
        ings.append(list(map(int, input().split())))
    for k, v in enumerate(ings):
        check(v[0], v[1], k)
    print(m[0])