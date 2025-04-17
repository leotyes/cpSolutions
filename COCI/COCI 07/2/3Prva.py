import sys
input = sys.stdin.readline

r, c = map(int, input().split())
rc = [ list(input()) for x in range(r) ]
columns = [ list(x) for x in zip(*rc) ]
words = []

for i in rc:
    nl = "".join(i).split("#")
    nl[-1] = nl[-1].strip()
    for j in nl:
        if len(j) > 1:
            words.append(j)

for i in columns:
    nl = "".join(i).split("#")
    nl[-1] = nl[-1].strip()
    for j in nl:
        if len(j) > 1:
            words.append(j)

print(sorted(words)[0])