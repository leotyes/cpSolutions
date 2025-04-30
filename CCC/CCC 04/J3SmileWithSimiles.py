n = int(input())
m = int(input())
nn = []
mm = []

for i in range(n):
    nn.append(input())

for i in range(m):
    mm.append(input())

for i in nn:
    for j in mm:
        print(i + " as " + j)