import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = list(map(int, input().strip().split()))
    if n[2] - n[1] == n[1] - n[0]:
        diff = n[1] - n[0]
        print((diff * (n[3] - 1) + n[0]) % (10**9 + 7))
    else:
        fact = n[1] // n[0]
        print(int(pow(fact, n[3] - 1, 10**9 + 7) * n[0] % (10**9 + 7)))