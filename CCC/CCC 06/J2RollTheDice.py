m = int(input())
n = int(input())
c = 0

for i in range(1, min(10, m + 1)):
    if 10 - i <= n:
        c += 1

if c > 1:
    print("There are " + str(c) + " ways to get the sum 10.")
elif c == 0:
    print("There are 0 ways to get the sum 10.")
else:
    print("There is 1 way to get the sum 10.")