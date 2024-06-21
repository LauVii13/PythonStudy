n = input()
h, q, nine = ord("H"), ord("Q"), ord("9")

output = False

for e in n:
    i = ord(e)
    if i == h or i == q or i == nine:
        output = True
        break

if output:
    print("YES")
else:
    print("NO")
