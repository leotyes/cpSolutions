n = int(input())
vi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for i in range(n):
    oc = input()
    nc = ""
    ints = []
    for j in range(len(oc)):
        if oc[j] in vi:
            if j == 0:
                ints.append(str(oc[j]))
            elif oc[j - 1] == "-":
                ints[len(ints) - 1] = ints[len(ints) - 1] + str(oc[j])
            elif oc[j - 1] in vi:
                ints[len(ints) - 1] = ints[len(ints) - 1] + str(oc[j])
            else:
                ints.append("+" + str(oc[j]))
        elif oc[j] == "-":
            ints.append(str(oc[j]))
    for j in range(len(oc)):
        if oc[j] != "-" and oc[j] not in vi and oc[j].lower() != oc[j]:
            nc = nc + oc[j]
    print(nc + str(eval("".join(ints))))