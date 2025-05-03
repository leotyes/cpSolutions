import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
stc = [ list(map(int, input().strip().split())) for x in range(n)]
abpm = [ list(map(int, input().strip().split())) for x in range(m)]
t = [0] * 101
mm = [99999999]

for i in stc:
    for j in range(i[0], i[1] + 1):
        t[j] = i[2]

def cool(c, cc, co):
    co += abpm[cc][3]
    tr = abpm[cc][2]
    for i in range(abpm[cc][0], abpm[cc][1] + 1):
        c[i] = max(c[i] - tr, 0)
    if c == [0] * 101:
        mm[0] = min(mm[0], co)
    else:
        for i in range(cc + 1, m):
            cool(c[:], i, co)

for i in range(m):
    cool(t[:], i, 0)

print(mm[0])