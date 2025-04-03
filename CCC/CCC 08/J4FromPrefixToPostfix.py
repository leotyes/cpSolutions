import sys
input = sys.stdin.readline
c = 0

while True:
    prefix = input().split()
    postfix = prefix[::-1]
    new = []
    if prefix[0] == "0":
        break
    else:
        for k, v in enumerate(postfix):
            if type(v) != list and not v.isdigit():
                if c == 0:
                    new.append(v)
                    new.append(postfix[k - 2])
                    new.append(postfix[k - 1])
                    c += 1
                    # consider case where the number is right next to the sign
                else:
                    new.insert(0, postfix[k - len(new) - 1])
                    new.insert(0, v)
        new = new[::-1]
    print(new)