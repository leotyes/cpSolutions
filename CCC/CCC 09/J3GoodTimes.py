o = int(input())
last = -1

print(str(o) + " in Ottawa")
if o - 300 < 0:
    print(str(2400 + o - 300) + " in Victoria")
else:
    print(str(o - 300) + " in Victoria")
if o - 200 < 0:
    print(str(2400 + o - 200) + " in Edmonton")
else:
    print(str(o - 200) + " in Edmonton")
if o - 100 < 0:
    print(str(2400 + o - 100) + " in Winnipeg")
else:
    print(str(o - 100) + " in Winnipeg")
print(str(o) + " in Toronto")
if o + 100 >= 2400:
    print(str((o + 100) % 2400) + " in Halifax")
else:
    print(str(o + 100) + " in Halifax")
if o + 130 >= 2400:
    if int(str((o + 130) % 2400)[-2]) >= 6:
        test = list(str((o + 130) % 2400))
        tojoin = []
        if test[:-2] == []:
            tojoin.append("1")
        else:
            tojoin.append(str(int("".join(test[:-2])) + 1))
        tojoin.append(str(int("".join(test[-2:])) % 60))
        print("".join(tojoin) + " in St. John's")
elif o + 130 >= 2360:
    print(str((o + 130) % 2360) + " in St. John's")
elif int(str(o)[-2]) + 3 >= 6:
    tojoin = []
    test = list(str(o + 130))
    if test[:-2] == []:
        tojoin.append("1")
    else:
        tojoin.append(str(int("".join(test[:-2])) + 1))
    tojoin.append(str(int(str(int(str(o)[-2]) + 3) + str(o)[-1]) % 60))
    if int(str(o)[-2]) + 3 == 6:
        tojoin.append("0")
    print("".join(tojoin) + " in St. John's")
else:
    print(str(o + 130) + " in St. John's")