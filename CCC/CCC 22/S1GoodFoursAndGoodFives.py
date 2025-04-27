c = 0
n = int(input())
r = n % 4
l = n // 4 + 1

for i in range(l):
    f = i
    ts = 4 * f
    ff = n - ts
    if ff % 5 == 0:
        c += 1

print(c)