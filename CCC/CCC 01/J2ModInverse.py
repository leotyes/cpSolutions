x = int(input())
m = int(input())

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if gcd(m, x) != 1:
    print("No such integer exists.")
else:
    y = 0
    while (x * y) % m != 1:
        y += 1
    print(y)