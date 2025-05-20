n = input()
nn = {"C": [], "D": [], "H": [], "S": []}
pt = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "A": 4, "K": 3, "Q": 2, "J": 1}
c = False
d = False
h = False
s = False
t = 0

for i in n:
    if not c:
        if i == "D":
            c = True
        elif i != "C":
            nn["C"].append(i)
    elif not d:
        if i == "H":
            d = True
        else:
            nn["D"].append(i)
    elif not h:
        if i == "S":
            h = True
        else:
            nn["H"].append(i)
    else:
        nn["S"].append(i)

print("Cards Dealt              Points")
cb = "Clubs " + " ".join(nn["C"])
cp = 0
if len(nn["C"]) == 0:
    cp += 3
elif len(nn["C"]) == 1:
    cp += 2
    cp += pt[nn["C"][0]]
elif len(nn["C"]) == 2:
    cp += 1
    cp += pt[nn["C"][0]]
    cp += pt[nn["C"][1]]
else:
    for i in nn["C"]:
        cp += pt[i]
print(cb + " " + str(cp))

db = "Diamonds " + " ".join(nn["D"])
dp = 0
if len(nn["D"]) == 0:
    dp += 3
elif len(nn["D"]) == 1:
    dp += 2
    dp += pt[nn["D"][0]]
elif len(nn["D"]) == 2:
    dp += 1
    dp += pt[nn["D"][0]]
    dp += pt[nn["D"][1]]
else:
    for i in nn["D"]:
        dp += pt[i]
print(db + " " + str(dp))

hb = "Hearts " + " ".join(nn["H"])
hp = 0
if len(nn["H"]) == 0:
    hp += 3
elif len(nn["H"]) == 1:
    hp += 2
    hp += pt[nn["H"][0]]
elif len(nn["H"]) == 2:
    hp += 1
    hp += pt[nn["H"][0]]
    hp += pt[nn["H"][1]]
else:
    for i in nn["H"]:
        hp += pt[i]
print(hb + " " + str(hp))

sb = "Spades " + " ".join(nn["S"])
sp = 0
if len(nn["S"]) == 0:
    sp += 3
elif len(nn["S"]) == 1:
    sp += 2
    sp += pt[nn["S"][0]]
elif len(nn["S"]) == 2:
    sp += 1
    sp += pt[nn["S"][0]]
    sp += pt[nn["S"][1]]
else:
    for i in nn["S"]:
        sp += pt[i]
print(sb + " " + str(sp))
t = cp + dp + hp + sp
print("                       Total " + str(t))