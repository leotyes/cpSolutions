l = []

for i in range(int(input())):
    l.append(int(input()))

l = [ str(x) for x in sorted(l)]
print("\n".join(l))