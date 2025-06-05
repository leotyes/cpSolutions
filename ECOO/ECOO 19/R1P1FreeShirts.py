import sys
input = sys.stdin.readline

for i in range(10):
    n, m, d = map(int, input().strip().split())
    nm = n
    a = sorted(list(map(int, input().strip().split())), reverse=True)
    c = 0
    ns = [0] * (d + 1)
    ns[1] = nm
    while len(a) != 0 and a[-1] == 1:
        nm += 1
        ns[1] += 1
        a.pop()
    for j in range(2, d + 1):
        while len(a) != 0 and a[-1] == j:
            nm += 1
            ns[j] += 1
            a.pop()
        if ns[j - 1] == 1:
            c += 1
            ns[j] += nm
        else:
            ns[j] += ns[j - 1] - 1
    print(c)