n, k = map(int, input().split())
s = list(input())
c = 0
r = 0
f = False

for ki, v in enumerate(s):
    if v == "P":
        c += 2
        r += 1
        if r > k:
            print("NO")
            f = True
            break
        if ki < len(s) - 1:
            if s[ki + 1] == "P":
                print("NO")
                f = True
                break
    elif v == "S":
        r += 1
        c += 1
        if r > k:
            print("NO")
            f = True
            break
    else:
        r = 0

if not f:
    print("YES")
    print(c)