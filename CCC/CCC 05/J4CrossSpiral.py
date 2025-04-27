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

# def walk(px, py):
#     if px == 3 and py == 6:
#         st[1] = True
#     if st[0] == s:
#         print(px + 1)
#         print(py + 1)
#     else:
#         st[0] += 1
#         xy[py][px] = "x"
#         if px != x - 1 and xy[py][px + 1] == "o":
#             walk(px + 1, py)
#         elif py != y - 1 and xy[py + 1][px] == "o":
#             walk(px, py + 1)
#         elif px != 0 and xy[py][px - 1] == "o":
#             walk(px - 1, py)
#         elif py != 0 and xy[py - 1][px] == "o":
#             walk(px, py - 1)
#
# walk(cx, 0)

def walk(px, py, d):
    if st[0] == s:
        print(px + 1)
        print(py + 1)
    else:
        st[0] += 1
        xy[py][px] = "x"
        if d % 12 == 1 or d % 12 == 3 or d % 12 == 11:
            if d % 12 == 11:
                if py != 0 and xy[py - 1][px] == "o":
                    walk(px, py - 1, d + 1)
                else:
                    if xy[py][px + 1] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px + 1, py, d)
            else:
                if px != x - 1 and xy[py][px + 1] == "o":
                    walk(px + 1, py, d)
                else:
                    if xy[py + 1][px] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px, py + 1, d + 1)
        elif d % 12 == 2 or d % 12 == 4 or d % 12 == 6:
            if d % 12 == 2:
                if px != x - 1 and xy[py][px + 1] == "o":
                    walk(px + 1, py, d + 1)
                else:
                    if xy[py + 1][px] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px, py + 1, d)
            else:
                if py != y - 1 and xy[py + 1][px] == "o":
                    walk(px, py + 1, d)
                else:
                    if xy[py][px - 1] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px - 1, py, d + 1)
        elif d % 12 == 5 or d % 12 == 7 or d % 12 == 9:
            if d % 12 == 5:
                if py != y - 1 and xy[py + 1][px] == "o":
                    walk(px, py + 1, d + 1)
                else:
                    if xy[py][px - 1] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px - 1, py, d)
            else:
                if py != 0 and xy[py][px - 1] == "o":
                    walk(px - 1, py, d)
                else:
                    if xy[py - 1][px] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px, py - 1, d + 1)
        elif d % 12 == 8 or d % 12 == 10 or d % 12 == 0:
            if d % 12 == 8:
                if px != 0 and xy[py][px - 1] == "o":
                    walk(px - 1, py, d + 1)
                else:
                    if xy[py - 1][px] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px, py - 1, d)
            else:
                if py != 0 and xy[py - 1][px] == "o":
                    walk(px, py - 1, d)
                else:
                    if xy[py][px + 1] == "x":
                        print(px + 1)
                        print(py + 1)
                    else:
                        walk(px + 1, py, d + 1)

walk(cx, 0, 1)