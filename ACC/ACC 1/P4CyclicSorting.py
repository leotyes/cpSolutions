import sys
input = sys.stdin.readline

n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

bs = set()
for k, v in enumerate(a):
    if k != 0:
        if v < a[k - 1]:
            bs.add(k)
    elif v < a[-1]:
        bs.add(k)
for j in range(q):
    i, x = map(int, input().strip().split())
    a[i - 1] = x
    if a[(i - 2) % n] > a[i - 1]:
        bs.add(i - 1)
    else:
        bs.discard(i - 1)

    if a[i - 1] > a[i % n]:
        bs.add(i % n)
    else:
        bs.discard(i % n)

    if len(bs) >= 2:
        print("-1")
    elif len(bs) == 1:
        print(min(list(bs)[0], len(a) - list(bs)[0]))
    else:
        print("0")