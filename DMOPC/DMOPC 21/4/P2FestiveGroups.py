import sys
input = sys.stdin.readline

n = int(input())
ji = sorted(set(map(int, input().split())))
jb = [True] * (ji[-1] + 1)
groups = 0

for z in ji:
    if jb[z]:
        groups += 1
        for i in range(z, len(jb), z):
            jb[i] = False

print(groups)