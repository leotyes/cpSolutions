import sys

sys.setrecursionlimit(2000000000)
r = int(input())
c = int(input())
rows = []
keys = {"S": 1, "M": 5, "L": 10, "*": "*"}
total = 0

for i in range(r):
    row = list(input())
    for j in range(len(row)):
        row[j] = keys[row[j]]
    rows.append(row)

a = int(input())
b = int(input())

def dfs(coords):
    total = 0
    total += rows[coords[0]][coords[1]]
    rows[coords[0]][coords[1]] = "*"
    if coords[0] - 1 >= 0 and rows[coords[0] - 1][coords[1]] != "*":
        total += dfs([coords[0] - 1, coords[1]])
    if coords[0] + 1 < r and rows[coords[0] + 1][coords[1]] != "*":
        total += dfs([coords[0] + 1, coords[1]])
    if coords[1] + 1 < c and rows[coords[0]][coords[1] + 1] != "*":
        total += dfs([coords[0], coords[1] + 1])
    if coords[1] - 1 >= 0 and rows[coords[0]][coords[1] - 1] != "*":
        total += dfs([coords[0], coords[1] - 1])
    return total

total += dfs([a, b])
print(total)