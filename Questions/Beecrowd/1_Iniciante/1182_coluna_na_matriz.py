col = int(input())
matriz = [[0 for i in range(12)] for j in range(12)]

op = input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

soma = 0
for i in range(12):
    soma += matriz[i][col]

if op == "S":
    print(f"{soma:.1f}")
else:
    print(f"{(soma / 12):.1f}")
