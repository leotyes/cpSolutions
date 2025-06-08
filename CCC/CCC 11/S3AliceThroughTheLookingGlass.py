t = int(input())
f = [(1, 0), (2, 0), (3, 0), (2, 1)]
p = [(1, 1), (3, 1), (2, 2)]

def crystal(m, x, y, cl):
    if m == 1:
        if (x, y) in f:
            print("crystal")
        else:
            print("empty")
    else:
        if (x // (5 ** (m - 1)), y // (5 ** (m - 1))) in f:
            print("crystal")
        elif (x // (5 ** (m - 1)), y // (5 ** (m - 1))) in p:
            nx, ny = x % (5 ** (m - 1)), y % (5 ** (m - 1))
            m -= 1
            cl += 1
            crystal(m, nx, ny, cl)
        else:
            print("empty")


for i in range(t):
    m, x, y = map(int, input().split())
    crystal(m, x, y, 1)