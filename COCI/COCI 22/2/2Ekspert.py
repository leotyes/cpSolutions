distance = int(input())
clubs = [int(input()) for a in range(int(input()))]
leaststrokes = [9999 for b in range(distance + 1)]
leaststrokes[0] = 0

for i in range(distance + 1):
    for j in range(len(clubs)):
        if i + clubs[j] <= distance:
            if leaststrokes[i] + 1 < leaststrokes[i + clubs[j]]:
                leaststrokes[i + clubs[j]] = leaststrokes[i] + 1

if leaststrokes[distance] < 9999:
    print("Roberta wins in " + str(leaststrokes[distance]) + " strokes.")
else:
    print("Roberta acknowledges defeat.")
