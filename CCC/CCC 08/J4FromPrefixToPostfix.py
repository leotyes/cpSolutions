import sys
input = sys.stdin.readline

s = []

while True:
    prefix = input().split()
    if prefix[0] == "0":
        break
    for i in reversed(prefix):
        if i.isdigit():
            s.append(i)
        else:
            o1 = s.pop()
            o2 = s.pop()
            s.append(o1 + o2 + i)
    print(" ".join(list(s.pop())))