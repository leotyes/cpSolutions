n = int(input())
cheese = [2, 3, 22, 23, 32, 33]
new = []
counter = 0

if n < 100:
    for i in cheese:
        if i <= n:
            counter += 1
        else:
            break
else:
    counter += 5
    for i in range(3, len(str(n)) - 1):
        counter += 2 ** i
    minn = "2" * len(str(n))