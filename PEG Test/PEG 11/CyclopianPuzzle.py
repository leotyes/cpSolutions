n = int(input())

def hanoi(r, a, b, c):
    if r == 1:
        print(a + c)
    else:
        hanoi(r - 1, a, c, b)
        print(a + c)
        hanoi(r - 1, b, a, c)

hanoi(n, "A", "B", "C")