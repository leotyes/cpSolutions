n = int(input())
preferred = list(map(int, input().split()))
current = list(map(int, input().split()))
ptoc = []
rt = 0
ans = 0
diff = []

for i in range(n):
    ptoc.append(preferred[i] - current[i])

for k, v in enumerate(ptoc):
    if k == 0:
        diff.append(v)
        rt += v
    else:
        diff.append(v - ptoc[k - 1])
        rt += v - ptoc[k - 1]

diff.append(-rt)

for i in diff:
    if i > 0:
        ans += i

print(ans)