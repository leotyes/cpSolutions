w = int(input())
counter = 0
toprint = ""

for i in range(97, 97 + min(w, 26)):
    toprint += chr(i) + " "
    counter += 1

for i in range(97, 123):
    for j in range(97, 123):
        if counter == w:
            break
        toprint += chr(i) + chr(j) + " "
        counter += 1
    if counter == w:
        break

for i in range(97, 123):
    for j in range(97, 123):
        for v in range(97, 123):
            if counter == w:
                break
            toprint += chr(i) + chr(j) + chr(v) + " "
            counter += 1
        if counter == w:
            break
    if counter == w:
        break

print(toprint)