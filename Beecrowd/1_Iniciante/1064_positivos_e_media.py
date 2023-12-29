count = 0
som = 0
for i in range(6):
    n = float(input())
    if n > 0:
        count += 1
        som += n

media = som / count

print(f"{count} valores positivos")
print(f"{media:.1f}")