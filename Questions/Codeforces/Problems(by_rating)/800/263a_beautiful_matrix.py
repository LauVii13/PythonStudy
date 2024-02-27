matriz = []

for i in range(5):
    matriz.append(list(map(int, input().split())))

for i in range(5):
    if 1 in matriz[i]:
        j = matriz[i].index(1)
        break

print(abs(i - 2) + abs(j - 2))
