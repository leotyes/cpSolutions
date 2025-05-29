q = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
c = 0

while q != 0:
    if c % 3 == 0:
        p1 += 1
        if p1 % 35 == 0:
            q += 30
    elif c % 3 == 1:
        p2 += 1
        if p2 % 100 == 0:
            q += 60
    elif c % 3 == 2:
        p3 += 1
        if p3 % 10 == 0:
            q += 9
    c += 1
    q -= 1

print("Martha plays " + str(c) + " times before going broke.")