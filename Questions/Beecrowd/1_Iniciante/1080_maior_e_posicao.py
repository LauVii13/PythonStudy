values = []
for i in range(100):
    values.append(int(input()))

maior = max(values)

print(maior)
print(values.index(maior) + 1)