import sys
input = sys.stdin.readline

for i in range(int(input())):
    l = []
    for j in range(4):
        ll = input().strip().lower().split()[-1][::-1]
        for k, v in enumerate(ll):
            if v in ["a", "e", "i", "o", "u"]:
                l.append(ll[:(k + 1)][::-1])
                break
        if len(l) != j + 1:
            l.append(ll)
    if l == [l[0]] * 4:
        print("perfect")
    elif l[0] == l[1] and l[2] == l[3]:
        print("even")
    elif l[0] == l[2] and l[1] == l[3]:
        print("cross")
    elif l[0] == l[3] and l[1] == l[2]:
        print("shell")
    else:
        print("free")