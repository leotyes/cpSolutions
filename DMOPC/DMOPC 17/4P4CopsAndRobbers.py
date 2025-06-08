n = int(input())
a = list(map(int, input().split()))
f = False

if a == [a[0]] * n:
    print("-1")
else:
    b = [ x for x in range(1, n + 1) ]
    for k, v in enumerate(b):
        if v == a[k]:
            if k == n - 1:
                b[k - 1], b[k] = b[k], b[k - 1]
                if b[k - 1] == a[k - 1]:
                    f = True
                break
            b[k], b[k + 1] = b[k + 1], b[k]
    if not f:
        print(*b)
    else:
        print("-1")