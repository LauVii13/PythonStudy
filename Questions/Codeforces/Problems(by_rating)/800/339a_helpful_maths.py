numbers = list(map(int, input().split("+")))

numbers.sort()
out = ""
for n in numbers:
    out += f"{n}+"

out = out[:-1]

print(out)
