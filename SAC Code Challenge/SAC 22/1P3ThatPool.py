import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nm = []

for i in range(n):
    nm.append(list(input().strip()))

q = int(input())
for i in range(q):
    a = int(input())
    if a == 1:
        for k, v in enumerate(reversed(nm)):
            ak = n - 1 - k
            if ak != 0:
                if ak == n - 1:
                    for kj, vj in enumerate(nm[ak]):
                        if vj == "X":
                            nm[ak][kj] = "."
                for kj, vj in enumerate(nm[ak - 1]):
                    if vj == "X":
                        nm[ak][kj] = "X"
                        nm[ak - 1][kj] = "."
        s = False
        while not s:
            s = True
            for k, v in enumerate(nm):
                ss = False
                while not ss:
                    ss = True
                    for kk, vk in enumerate(v):
                        if kk != 0 and vk == "W" and v[kk - 1] == ".":
                            nm[k][kk] = "."
                            nm[k][kk - 1] = "W"
                            ss = False
                            s = False
            ig = []
            for k, v in enumerate(nm):
                if k != n - 1:
                    for kk, vk in enumerate(v):
                        if nm[k][kk] == "W" and nm[k + 1][kk] == "." and (k, kk) not in ig:
                            nm[k][kk] = "."
                            nm[k + 1][kk] = "W"
                            ig.append((k + 1, kk))
                            s = False
    else:
        for j in nm:
            print(*j, sep="")