n = int(input())

def oneMore(number):
    print(n - number + 1)
    if number != 1:
        oneMore(number - 1)

def oneLess(number):
    print(number)
    if number != 1:
        oneLess(number - 1)
        print(number)
    else:
        print(1)

oneLess(n)