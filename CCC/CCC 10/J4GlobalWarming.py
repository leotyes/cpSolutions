import sys
input = sys.stdin.readline
broken = False
found = False

while True:
    n = list(map(int, input().split()))
    broken = False
    found = False
    diff = []
    if n[0] == 0:
        break
    else:
        first = n[0]
        del n[0]
        for i in range(first - 1):
            diff.append(n[i + 1] - n[i])
        for i in range(1, first - 1):
            for j in range(first - 1):
                if diff[j] != diff[j % i]:
                    broken = True
                    break
            if broken:
                broken = False
                continue
            else:
                found = True
                print(i)
                break
        if not found:
            print(first - 1)