d = int(input())
e = int(input())
te = []

for i in range(2 * e):
    te.append(input())

print(eval("".join(te)) + d)