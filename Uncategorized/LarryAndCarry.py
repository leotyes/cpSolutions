n = []
m = [-1]

for i in range(int(input())):
    n.append(input())

def search(k, v, c):
    a = v[::-1]
    for z in range(k + 1, len(n)):
        fail = False
        b = n[z][::-1]
        for j in range(min(len(a), len(b))):
            if int(a[j]) + int(b[j]) >= 10:
                fail = True
                break
        if not fail:
            m[0] = max(m[0], c + 1)
            search(z, str(int(a[::-1]) + int(b[::-1])), c + 1)

for k, v in enumerate(n):
    search(k, v, 1)

print(m[0])