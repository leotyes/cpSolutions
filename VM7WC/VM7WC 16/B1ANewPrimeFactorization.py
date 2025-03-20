import math

y = int(input())

for i in range(2, int(math.sqrt(y) // 1) + 1):
    while y % i == 0:
        print(i)
        y = y / i

if y != 1:
    print(int(y))