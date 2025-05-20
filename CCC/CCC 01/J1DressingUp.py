n = int(input())

for i in range(1, n, 2):
    print("*" * i + " " * (2 * n - i * 2) + "*" * i)

print("*" * (2 * n))

for i in range(n - 2, -1, -2):
    print("*" * i + " " * (2 * n - i * 2) + "*" * i)