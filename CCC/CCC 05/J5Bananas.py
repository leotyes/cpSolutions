import sys
input = sys.stdin.readline

while True:
    word = list(input().strip())
    if len(word) == 1 and word[0] == "A":
        print("YES")
        continue
    elif word[0] == "X":
        break
    else:
        while word != []:
            if word[:2] == ["A", "N"]:
                del word[:2]
            elif word[:2] == ["B", "S"]:
                print("NO")
                break
            elif word[0] == "B" and word[-1] == "S":
                del word[0]
                del word[-1]
            elif word[0] == "A":
                if len(word) == 1:
                    print("YES")
                    break
                elif word[1] != "N":
                    del word[0]
            else:
                print("NO")
                break
        if word == []:
            print("YES")