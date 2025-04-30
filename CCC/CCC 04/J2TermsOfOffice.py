x = int(input())
y = int(input())
c = 0

while True:
    print("All positions change in year " + str(x + c * 60))
    c += 1
    if x + c * 60 > y:
        break