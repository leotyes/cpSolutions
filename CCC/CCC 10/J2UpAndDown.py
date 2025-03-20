a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
counter = 0
nikky = 0
nikkyc = 0
byron = 0
byronc = 0

while nikkyc < s and byronc < s:
    if counter % 2 == 0:
        if nikkyc + a >= s:
            nikky += s - nikkyc + 1
        else:
            nikky += a
        nikkyc += a
        if byronc + c >= s:
            byron += s - byronc + 1
        else:
            byron += c
        byronc += c
    else:
        if nikkyc + b >= s:
            nikky -= s - nikkyc + 1
        else:
            nikky -= b
        nikkyc += b
        if byronc + d >= s:
            byron -= s - byronc + 1
        else:
            byron -= d
        byronc += d
    counter += 1

if nikky > byron:
    print("Nikky")
elif nikky == byron:
    print("Tied")
else:
    print("Byron")