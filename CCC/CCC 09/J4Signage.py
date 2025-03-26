w = int(input())
letters = [7, 2, 3, 4, 4, 5]
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
printing = []
spaces = []
counter = w
other = 0

while True:
    printing = []
    spaces = []
    counter = w
    other = 0
    for k, v in enumerate(letters):
        if counter - v >= 0:
            counter -= v
            other += v
            printing.append(words[k])
        else:
            break
    other += len(printing) - 1
    spaces = ["."] * (len(printing) - 1)
    for i in range(w - other):
        spaces[(i % len(spaces)) - 1] + "."
    for i in range(len(printing) + len(spaces)):
        if i % 2 == 0:
            print(printing[i / 2])
        else:
            print(spaces[(i - 1) / 2])
    toremove = [ k for k, v in words if k <= len(printing)]
    for k, v in enumerate(printing):
        words.remove(v)
        del letters
    break