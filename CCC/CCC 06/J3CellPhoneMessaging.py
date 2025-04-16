import sys
input = sys.stdin.readline

c = 0
r = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

while True:
    c = 0
    n = list(input())
    if n == ["h", "a", "l", "t", "\n"]:
        break
    for k, v in enumerate(n):
        for i in r:
            if v in i:
                if n[k + 1] in i:
                    c += 2
                c += i.index(v) + 1
                break
    print(c)