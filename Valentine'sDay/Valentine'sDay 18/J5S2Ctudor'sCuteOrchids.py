import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = [ int(input()) for x in range(n) ]
d = [ list(map(int, input().strip().split())) for x in range(m) ]
r = list(map(int, input().strip().split()))
mc = [999999999999]

def deal(rr, cc, ci):
    ccc = cc
    if cc < mc[0]:
        for k, v in enumerate(rr):
            ccc += v * c[k]
        mc[0] = min(mc[0], ccc)
        ccc = cc
        for i in range(ci, len(d)):
            ccc = cc
            rrr = rr[:]
            ccc += d[i][0]
            b = False
            for k, v in enumerate(rrr):
                rrr[k] -= d[i][k + 1]
                if rrr[k] < 0:
                    b = True
                    break
            if not b:
                cccc = ccc
                for k, v in enumerate(rrr):
                    cccc += v * c[k]
                mc[0] = min(mc[0], cccc)
                deal(rrr[:], ccc, i + 1)

deal(r[:], 0, 0)
print(mc[0])