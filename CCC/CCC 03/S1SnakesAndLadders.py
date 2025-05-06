import sys
input = sys.stdin.readline

c = 1
s = {54: 19, 90: 48, 99: 77}
l = {9: 34, 40: 64, 67: 86}

while True:
    n = int(input())
    c += n
    if n == 0:
        print("You Quit!")
        break
    elif c in s.keys():
        c = s[c]
    elif c in l.keys():
        c = l[c]
    elif c > 100:
        c -= n
    elif c == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    print("You are now on square " + str(c))