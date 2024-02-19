t = int(input())

for _ in range(t):
    letters = input()
    tot = letters.count("A")

    if tot >= 3:
        print("A")
    else:
        print("B")
