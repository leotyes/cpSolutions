p = int(input())
g = int(input())
r = int(input())
o = int(input())
n = int(input())
e = set()
m = 9999999

def sell(cp, cg, cr, co, cn):
    if cn < n:
        sell(cp + 1, cg, cr, co, cn + p)
        sell(cp, cg + 1, cr, co, cn + g)
        sell(cp, cg, cr + 1, co, cn + r)
        sell(cp, cg, cr, co + 1, cn + o)
    elif cn == n:
        e.add((cp, cg, cr, co))

sell(0, 0, 0, 0, 0)
for i in e:
    m = min(m, i[0] + i[1] + i[2] + i[3])
    print("# of PINK is " + str(i[0]) + " # of GREEN is " + str(i[1]) + " # of RED is " + str(i[2]) + " # of ORANGE is " + str(i[3]))

print("Total combinations is " + str(len(e)) + ".")
print("Minimum number of tickets to print is " + str(m) + ".")