trout = int(input())
pike = int(input())
pickerel = int(input())
total = int(input())
counter = 0

for i in range(total // trout + 1):
    for j in range(total // pike + 1):
        for k in range(total // pickerel + 1):
            if i * trout + j * pike + k * pickerel <= total:
                if i != 0 or j != 0 or k != 0:
                    counter += 1
                    print(str(i) + " Brown Trout, " + str(j) + " Northern Pike, " + str(k) + " Yellow Pickerel")

print("Number of ways to catch fish: " + str(counter))