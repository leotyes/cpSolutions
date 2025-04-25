x = int(input())
y = int(input())
cx = int(input())
cy = int(input())
s = int(input())
st = [0, False]
xy = [ [ "o" for a in range(x) ] for z in range(y) ]

for i in range(y):
    for j in range(x):
        if i < cy or y - i - 1 < cy:
            if j < cx or x - j - 1< cx:
                xy[i][j] = "x"

def walk(px, py):
    if px == 3 and py == 6:
        st[1] = True
    if st[0] == s:
        print(px + 1)
        print(py + 1)
    else:
        st[0] += 1
        xy[py][px] = "x"
        if px != x - 1 and xy[py][px + 1] == "o":
            walk(px + 1, py)
        elif py != y - 1 and xy[py + 1][px] == "o":
            walk(px, py + 1)
        elif px != 0 and xy[py][px - 1] == "o":
            walk(px - 1, py)
        elif py != 0 and xy[py - 1][px] == "o":
            walk(px, py - 1)

walk(cx, 0)