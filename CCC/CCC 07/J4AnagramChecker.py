a = input()
b = input()
d = {}
d2 = {}

for i in set(list("".join(a.split()))):
    d[i] = a.count(i)

for i in set(list("".join(b.split()))):
    d2[i] = b.count(i)

if d == d2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")