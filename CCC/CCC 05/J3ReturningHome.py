d = []
l = []

while True:
    dd = input()
    if dd == "R":
        d.append(True)
    else:
        d.append(False)
    ll = input()
    l.append(ll)
    if ll == "SCHOOL":
        break

new = [ list(x) for x in reversed(list(zip(d, l))) ]

for k, v in enumerate(new):
    dd = ""
    if v[0]:
        dd = "LEFT"
    else:
        dd = "RIGHT"
    if k == len(new) - 1:
        print("Turn " + dd + " into your HOME.")
    else:
        print("Turn " + dd + " onto " + new[k + 1][1] + " street.")