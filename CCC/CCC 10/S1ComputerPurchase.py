import sys
input = sys.stdin.readline

n = int(input())
rankings = {}
first = []
second = []

for i in range(n):
    c, r, s, d = input().split()
    r, s, d = map(int, [r, s, d])
    if n == 1:
        print(c)
        break
    else:
        rankings[c] = 2 * r + 3 * s + d

rankings = sorted(rankings.items(), key=lambda item: item[1], reverse=True)

if n != 1 and n != 0:
    for i in rankings:
        if rankings[0][0] != i[0]:
            if rankings[0][1] == i[1]:
                first.append(i)
            else:
                if rankings[1][0] != i[0]:
                    if rankings[1][1] == i[1]:
                        second.append(i)
                    else:
                        break
                else:
                    second.append(i)
        else:
            first.append(i)

    if len(first) > 1:
        first = sorted(first, key=lambda item: item[0])
        print(first[0][0])
        print(first[1][0])
    elif len(second) > 1:
        second = sorted(second, key=lambda item: item[0])
        print(rankings[0][0])
        print(second[0][0])
    else:
        print(rankings[0][0])
        print(rankings[1][0])