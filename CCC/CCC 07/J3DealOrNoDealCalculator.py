n = int(input())
cases = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000, 6: 25000, 7: 50000, 8: 100000, 9: 500000, 10: 1000000}

for i in range(n):
    del cases[int(input())]

d = int(input())

if d > sum(list(cases.values())) / len(list(cases.values())):
    print("deal")
else:
    print("no deal")