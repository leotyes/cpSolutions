z = int(input())

def construct(s, n, k):
    c = False
    if len(s) == n:
        print(s)
    else:
        for i in range(n - len(s), 0, -1):
            if len(s) == n - i and k == i:
                construct(s + "1" * i , n, k - i)
                c = True
                break
        if not c:
            if k != 0:
                construct(s + "1", n, k - 1)
            construct(s + "0", n, k)


for i in range(z):
    n, k = map(int, input().split())
    print("The bit patterns are")
    construct("", n, k)
    if i != z - 1:
        print("")