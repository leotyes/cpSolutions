a, b, k = map(int, input().split())
c = 1
f = False

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

firstgcd = gcd(a, b)

if k == 1:
    print(firstgcd)
    f = True
else:
    for i in range(int((firstgcd ** 0.5) // 1), 0, -1):
        if firstgcd % i == 0:
            c += 1
            if c == k:
                print(i)
                f = True
                break

if not f:
    print(-1)