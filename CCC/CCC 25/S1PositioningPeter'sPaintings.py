i = [ int(x) for x in input().split(" ") ]

p1 = 2 * (i[0] + i[2]) + 2 * max(i[1], i[3])
p2 = 2 * (i[1] + i[3]) + 2 * max(i[0], i[2])

print(min(p2, p1))