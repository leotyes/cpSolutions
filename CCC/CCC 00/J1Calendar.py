s, d = map(int, input().split())
c = 0
k = False

print("Sun Mon Tue Wed Thr Fri Sat")
r = " " * (((s - 1) * 4) - 1)
for i in range(1, 7 - s + 2):
    r += "   " + str(i)
if (((s - 1) * 4) - 1) == -1:
    r = r[1:]
c = 7 - s + 2
print(r)
for i in range(5):
    if k:
        break
    r = ""
    for j in range(c, c + 7):
        if j > d:
            k = True
            break
        else:
            if j <= 9:
                if j == c:
                    r += "  " + str(j)
                else:
                    r += "   " + str(j)
            else:
                if j == c:
                    r += " " + str(j)
                else:
                    r += "  " + str(j)
    c += 7
    print(r)