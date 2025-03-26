w = int(input())
letters = [7, 2, 3, 4, 4, 5]
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
test = 0
printing = []
spaces = []
toremove = []
finalline = ""
counter = w
other = 0

while True:
    test += 1
    printing = []
    spaces = []
    toremove = []
    finalline = ""
    counter = w
    other = 0
    for k, v in enumerate(letters):
        if k != 0:
            if counter - v - 1 >= 0:
                counter -= v + 1
                other += v
                printing.append(words[k])
            else:
                break
        else:
            if counter - v >= 0:
                counter -= v
                other += v
                printing.append(words[k])
            else:
                break
    other += len(printing) - 1
    spaces = ["."] * (len(printing) - 1)
    if w != 7:
        if len(spaces) == 0:
            spaces.append((w - len(printing[0])) * ".")
        else:
            for i in range(w - other):
                spaces[(i % len(spaces))] = spaces[(i % len(spaces)) - 1] + "."
    else:
        if test != 1:
            if len(spaces) == 0:
                spaces.append((w - len(printing[0])) * ".")
            else:
                for i in range(w - other):
                    spaces[(i % len(spaces))] = spaces[(i % len(spaces)) - 1] + "."
    for i in range(len(printing) + len(spaces)):
        if i % 2 == 0:
            finalline += printing[int(i / 2)]
        else:
            finalline += spaces[int((i - 1) / 2)]
    toremove = reversed([ k for k, v in enumerate(printing) ])
    for i in toremove:
        del words[i]
        del letters[i]
    print(finalline)
    if words == []:
        break