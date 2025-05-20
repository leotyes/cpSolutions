n = int(input())
r = []
c = [0]

def place(cs):
    ccs = cs[:]
    if len(cs) == n:
        c[0] += 1
    else:
        for i in range(n):
            if i not in ccs:
                b = False
                for k, v in enumerate(ccs):
                    if k + v == i + len(ccs) or k - v == len(ccs) - i:
                        b = True
                        break
                if not b:
                    ccs.append(i)
                    place(ccs)
                    ccs.pop()

place([])
print(c[0])