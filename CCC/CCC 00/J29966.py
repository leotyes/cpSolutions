m = int(input())
n = int(input())
d = {"9": "6", "6": "9", "1": "1", "8": "8", "0": "0"}
c = 0

for i in range(m, n + 1):
    t = ""
    b = False
    for j in str(i):
        if j in d:
            t += d[j]
        else:
            b = True
            break
    if b:
        continue
    elif t[::-1] == str(i):
        c += 1

print(c)