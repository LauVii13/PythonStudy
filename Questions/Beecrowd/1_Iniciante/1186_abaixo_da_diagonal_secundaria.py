matriz = [[0 for i in range(12)] for j in range(12)]

op = input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())



soma = 0
cont = 0
for i in range(12):
    for j in range(12):
        if j + i > 11:
            soma += matriz[i][j]
            cont += 1

if op == "S":
    print(f"{soma:.1f}")
else:
    print(f"{(soma / cont):.1f}")
