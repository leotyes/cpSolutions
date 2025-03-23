rle = input()
rlea = []
rlen = []
tojoin = []
c = int(input())
totallength = 0
current = 0
remainder = 0

for k, v in enumerate(rle):
    if v.isalpha():
        rlea.append(v)
        if k != 0:
            rlen.append(int("".join(tojoin)))
            tojoin = []
    else:
        tojoin.append(v)

rlen.append(int("".join(tojoin)))

for i in rlen:
    totallength += i

remainder = c % totallength

for k, v in enumerate(rlen):
    if current + v > remainder:
        print(rlea[k])
        break
    else:
        current += v