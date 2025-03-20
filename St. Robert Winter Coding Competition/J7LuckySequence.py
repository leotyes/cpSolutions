n = int(input())
aa = list(input())
del aa[-1]
a = [ int(x) for x in "".join(aa).split(" ") ]
k = int(input())
s = 0
even = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(i)

for i in range(len(even) - k + 1):
    upperU = len(a) - 1
    if i + k <= len(even) - 1:
        upperU = even[i + k] - 1
    upperB = even[i + k - 1]
    lowerU = even[i]
    lowerB = 0
    if i - 1 >= 0:
        lowerB = even[i - 1] + 1
    s += (lowerU - lowerB + 1) * (upperU - upperB + 1)

print(s)