s = ["A", "B", "C", "D", "E"]

while True:
    b = int(input())
    n = int(input())
    if b == 1:
        for i in range(n):
            s.append(s[0])
            del s[0]
    elif b == 2:
        for i in range(n):
            s.insert(0, s[-1])
            del s[-1]
    elif b == 3:
        for i in range(n):
            s[0], s[1] = s[1], s[0]
    elif b == 4:
        print(" ".join(s))
        break