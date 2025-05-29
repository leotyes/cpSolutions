n = int(input())

for i in range(n):
    w1 = input()
    w2 = input()
    w3 = input()
    if w1.startswith(w2) or w1.startswith(w3) or w2.startswith(w3) or w2.startswith(w1) or w3.startswith(w1) or w3.startswith(w2) or w3.startswith(w1) or w1.endswith(w2) or w1.endswith(w3) or w2.endswith(w3) or w2.endswith(w1) or w3.endswith(w1) or w3.endswith(w2):
        print("No")
    else:
        print("Yes")