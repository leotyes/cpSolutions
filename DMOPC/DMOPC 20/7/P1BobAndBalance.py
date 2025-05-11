n = int(input())
ns = list(map(int, input().split()))
nsi = [ x for x in range(1, (n * 2) + 1) ]
c = list(zip(ns, nsi))
c.sort()
ns, nsi = zip(*c)
ns1 = ns[:n]
ns2 = ns[n:]
nsi1 = nsi[:n]
nsi2 = nsi[n:]
cc = 0
p = []

for i in range(n):
    if ns1[i] != ns2[i]:
        cc += 1
    p.append(str(nsi1[i]) + " " + str(nsi2[i]))

print(cc)
for i in p:
    print(i)