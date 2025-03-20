import sys
input = sys.stdin.readline

n, p = map(int, input().split())
posts = []
fullmap = []

for i in range(p):
    posts.append(list(map(int, input().split())))

for i in range(max(posts, key=lambda item: item[1])[1] + 1):
    fullmap.append([])
    for j in range(max(posts, key=lambda item: item[0])[0] + 1):
        fullmap[i].append("o")

for k, v in enumerate(posts):
    if posts[k + 1][0] == v[0]:
        for i in range(min(posts[k + 1][0], v[0]), max(posts[k + 1][0], v[0])):
            fullmap[v[1]][i] = "x"