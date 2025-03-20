n = int(input())
a = input().split(" ")
s = 0

l = int(input())
r = int(input())

for i in range(r - l + 1):
    s += int(a[l + i])

if s % 2 == 0:
    print("Even")
else:
    print("Odd")