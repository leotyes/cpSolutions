import sys
input = sys.stdin.readline

n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

for j in range(q):
    i, x = map(int, input().strip().split())
    a[i - 1] = x
    b = 0
    kk = -1

    for k, v in enumerate(a):
        if k != 0:
            if v < a[k - 1]:
                b += 1
                kk = k
                if b == 2:
                    print("-1")
                    break
        elif a[-1] > v:
            b += 1
            kk = k
    if b == 0:
        print("0")
    elif b != 2:
        print(min(kk, len(a) - kk))