a, b = map(int, input().split())
c = 0
d = 1
p = a * b
l = ["A A B"]
o = 1

b = 2 * a

while True:
    if b == p:
        print(o)
        for i in l: print(str(i))
        print("B")
        break
    l.append("B B B")
    b *= 2
    o += 1
    if a + b == p:
        print(o + 1)
        l.append("A B C")
        for i in l: print(str(i))
        print("C")
        break