loop = True
ab = {"A": 0, "B": 0}

while loop:
    ixy = input().split()
    i = int(ixy[0])
    if i == 7:
        break
    elif len(ixy) == 3:
        x, y = ixy[1], ixy[2]
    else:
        x = ixy[1]
    if i == 1:
        ab[x] = int(y)
    elif i == 2:
        print(ab[x])
    elif i == 3:
        ab[x] += ab[y]
    elif i == 4:
        ab[x] *= ab[y]
    elif i == 5:
        ab[x] -= ab[y]
    elif i == 6:
        if ab[x] / ab[y] >= 0:
            ab[x] //= ab[y]
        else:
            ab[x] = -(-ab[x] // ab[y])