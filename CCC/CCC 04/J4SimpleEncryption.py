c = [ ord(x) - 65 for x in list(input()) ]
t = "".join(x for x in input() if x.isalpha())
n = ""

for k, v in enumerate(t):
    n += chr((ord(v) - 65 + (c[k % len(c)])) % 26 + 65)

print(n)