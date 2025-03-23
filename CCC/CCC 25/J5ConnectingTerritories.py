r = int(input())
c = int(input())
m = int(input())
mins0 = [ i % m + 1 for i in range(c) ]
mins1 = [ (c + i) % m + 1 for i in range(c) ]

for i in range(r - 1):
    for j in range(c):
        if j >= 1:
            if j + 1 < c:
                mins1[j] = min(mins0[j], mins0[j - 1], mins0[j + 1]) + mins1[j]
            else:
                mins1[j] = min(mins0[j], mins0[j - 1]) + mins1[j]
        else:
            mins1[j] = min(mins0[j], mins0[j + 1]) + mins1[j]
    mins0 = mins1
    mins1 = [ (i * c + x + c + c) % m + 1 for x in range(c) ]

print(min(mins0))