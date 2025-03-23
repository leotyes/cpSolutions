s = input()
ab = {"A": 0, "B": 0}

for i in range(len(s)):
    ab[s[i]] += 1

if ab["A"] == ab["B"]:
    print("Yes")
else:
    print("No")