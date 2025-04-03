gps = [["A", "B", "C", "D", "E", "F"], ["G", "H", "I", "J", "K", "L"], ["M", "N", "O", "P", "Q", "R"], ["S", "T", "U", "V", "W", "X"], ["Y", "Z", " ", "-", ".", "e"]]
w = input()
prev = [0, 0]
c = 0
current = []

for i in w:
    for k, v in enumerate(gps):
        if i in v:
            current = [k, v.index(i)]
    c += abs(current[0] - prev[0]) + abs(current[1] - prev[1])
    prev = current

c += abs(5 - prev[0]) + abs(4 - prev[1])
print(c)