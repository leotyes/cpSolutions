n = int(input())
dw = []
new = []
current = -1

for i in range(n):
    if input() == "S":
        dw.append(1)
    else:
        dw.append(0)

for i in range(len(dw)):
    if i == 0:
        new.append(str(dw[i]))
    elif dw[i - 1] == dw[i]:
        if dw[i] == 0:
            new[len(new) - 1] = new[len(new) - 1] + str(dw[i])
        else:
            new[len(new) - 1] = new[len(new) - 1] + "+" + str(dw[i])
    else:
        new.append(str(dw[i]))

for i in range(len(new)):
    if eval(new[i]) != 0:
        new[i] = eval(new[i])

if len(new) == 1:
    if int(new[0]) == 0:
        current = 1
    else:
        current = int(new[0]) - 1
elif len(new) == 2:
    if int(new[0]) != 0:
        current = int(new[0]) + 1
    else:
        current = new[1] + 1
else:
    for i in range(len(new)):
       if new[i] == "0":
            if i >= 1 and i + 1 < len(new):
                if new[i + 1] + 1 + new[i - 1] > current:
                    current = new[i + 1] + 1 + new[i - 1]
       elif int(new[i]) > 0:
             if new[i] + 1 > current:
                 if i >= 0 or i + 1 < len(new):
                    current = new[i] + 1
             elif new[i] > current:
                 current = new[i]

if current != -1:
    print(current)