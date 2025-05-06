import sys
input = sys.stdin.readline

while True:
    c = int(input())
    a, b = 0, 0
    if c == 0:
        break
    for i in range(int((c ** .5) // 1), 0, -1):
        if c % i == 0:
            a = i
            b = c / a
            break
    print("Minimum perimeter is " + str(int(a * 2 + b * 2)) + " with dimensions " + str(int(a)) + " x " + str(int(b)))