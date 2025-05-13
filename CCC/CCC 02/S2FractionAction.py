n = int(input())
d = int(input())

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if n % d == 0:
    print(int(n / d))
else:
    g = gcd(n % d, d)
    if n // d == 0:
        print(str(int((n % d) / g)) + "/" + str(int(d / g)))
    else:
        print(str(n // d) + " " + str(int((n % d) / g)) + "/" + str(int(d / g)))