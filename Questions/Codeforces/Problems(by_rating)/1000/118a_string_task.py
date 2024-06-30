word = [i for i in input().lower()]
vowels = ["a", "o", "y", "e", "u", "i"]
for i in word:
    if not i in vowels:
        print(f".{i}", end="")

print()
