n = input()
troublesome = input()
silly = []
nd = {}
td = {}
wd = []
tdd = ""

for i in n:
    if i in nd:
        continue
    else:
        nd[i] = n.count(i)

for i in troublesome:
    if i in td:
        continue
    else:
        td[i] = troublesome.count(i)

for i in nd:
    if not i in td:
        wd.append(i)

for i in td:
    if not i in nd:
        tdd = i

if len(wd) == 1:
    print(wd[0] + " " + tdd[0])
    print("-")
else:
    for i in range(len(n)):
        if n[i] in wd:
            if troublesome[i] == tdd:
                silly.append(n[i])
                silly.append(tdd)
                wd.remove(n[i])
                print(" ".join(silly))
                print(wd[0])
                break
            else:
                wd.remove(n[i])
                silly.append(wd[0])
                silly.append(tdd)
                print(" ".join(silly))
                print(n[i])
                breaktrou