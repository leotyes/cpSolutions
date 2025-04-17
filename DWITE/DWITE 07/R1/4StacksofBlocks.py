import sys
input = sys.stdin.readline

h = int(input())
s = int(input())
bs = [int(input()) for x in range(s)]
c = [999999]

def build(ch, b, r):
    nb = b + 1
    nh = ch
    if ch == h:
        c[0] = min(c[0], b)
    elif ch < h:
        for i in r:
            nh = ch
            j = r[:]
            nh += i
            j.remove(i)
            build(nh, nb, j)

build(0, 0, bs[:])
if c[0] == 999999:
    print(0)
else:
    print(c[0])