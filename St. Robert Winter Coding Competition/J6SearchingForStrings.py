t = input()
s = input()
dt = {}
ds = {}
kt = []
m = 99999999

for i in range(len(t)):
    dt[t[i]] = dt.get(t[i], 0) + 1

for i in range(len(s)):
    ds[s[i]] = ds.get(s[i], 0) + 1

kt = list(dt.keys())

for i in range(len(kt)):
    if kt[i] in ds:
        m = min(m, ds[kt[i]] // dt[kt[i]])
    else:
        m = 0
        break

print(m)