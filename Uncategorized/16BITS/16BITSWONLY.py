import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    a, b, p = map(int, input().strip().split())
    if a * b == p:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")