r = int(input())
c = int(input())
m = int(input())
mins = [[ i % m + 1 for i in range(c) ], [ (c + i) % m + 1 for i in range(c) ]]

for i in range(r - 1):
    for j in range(c):
        if j >= 1:
            if j + 1 < c:
                mins[1][j] = min(mins[0][j], mins[0][j - 1], mins[0][j + 1]) + mins[1][j]
            else:
                mins[1][j] = min(mins[0][j], mins[0][j - 1]) + mins[1][j]
        else:
            mins[1][j] = min(mins[0][j], mins[0][j + 1]) + mins[1][j]
    mins = [[ x for x in mins[1] ], [ (i * c + x + c + c) % m + 1 for x in range(c) ]]

print(min(mins[0]))