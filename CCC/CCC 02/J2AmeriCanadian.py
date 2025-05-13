v = ["a", "e", "i", "o", "u", "y"]

while True:
    n = input()
    if n == "quit!":
        break
    elif len(n) > 4 and n[-1] == "r" and n[-2] == "o" and not n[-3] in v:
        s = n[:-2]
        s += "our"
        print(s)
    else:
        print(n)