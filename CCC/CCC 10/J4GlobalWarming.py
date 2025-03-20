import sys
input = sys.stdin.readline

while True:
    compare = []
    failed = False
    n = list(map(int, input().split()))
    diff = []
    if n[0] == 0:
        break
    elif n[0] == 1 or n[0] == 2:
        print(n[0])
        continue
    else:
        l = n[0]
        n.remove(n[0])
        for i in range(l - 1):
            diff.append(n[i + 1] - n[i])
        print(diff)
        for i in range(2, l // 2):
            failed = False
            print(l % i)
            if l % i == 0:
                print("whtwiohifh")
                for j in range(i, l, i):
                    if j == i:
                        compare = n[j - i:i]
                    elif compare != n[j - i:i]:
                        failed = True
                        break
                if not failed:
                    print(i)
                    break