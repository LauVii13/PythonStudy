n = input()
chars = {}
cont = 0

for e in n:
    if chars.get(e, None) is not None:
        continue
    chars[e] = True
    cont += 1

if cont % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
