t = int(input())
s = int(input())
h = int(input())

ss = " " * s
tt = "*" + ss + "*" + ss + "*"

for i in range(t):
    print(tt)

print("*" * ((s * 2) + 3))

for i in range(h):
    print(" " * (s + 1) + "*")