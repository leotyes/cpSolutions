d = int(input())
e = int(input())
w = int(input())
a = (max(d - 100, 0) * 25 + 15 * e + 20 * w) / 100
b = (max(d - 250, 0) * 45 + 35 * e + 25 * w) / 100

print("Plan A costs " + "{:.2f}".format(a))
print("Plan B costs " + "{:.2f}".format(b))

if a < b:
    print("Plan A is cheapest.")
elif a == b:
    print("Plan A and B are the same price.")
else:
    print("Plan B is cheapest.")