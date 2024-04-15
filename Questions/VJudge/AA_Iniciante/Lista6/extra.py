import sys

sys.setrecursionlimit(2 * 10**5 + 81)


h, w = map(int, input().split())

# matriz = [[v for v in input()] for _ in range(h)]

matriz = []
for i in range(h):
    linha = input()
    matriz.append([])
    for j in range(w):
        matriz[i].append(linha[j])
        if linha[j] == "S":
            ini = (i, j)
        if linha[j] == "T":
            fim = (i, j)

distancia = abs(ini[0] - fim[0]) + abs(ini[1] - fim[1])

energia = 0
tot_medicines = int(input())
soma_med = 0
for i in range(tot_medicines):
    r, c, e = map(int, input().split())
    soma_med += e
    if matriz[r - 1][c - 1] == "S":
        energia = e
    else:
        matriz[r - 1][c - 1] = e

result = "No"

fila = []
fila.append((ini[0], ini[1], energia))

while fila:
    prox = fila[0]
    inicio, ener = (prox[0], prox[1]), prox[2]
    fila.pop(0)

    if matriz[inicio[0]][inicio[1]] == "T":
        print("Yes")
        exit()
    if matriz[inicio[0]][inicio[1]] != "." and matriz[inicio[0]][inicio[1]] != "S":
        ener = matriz[inicio[0]][inicio[1]]
        matriz[inicio[0]][inicio[1]] = "."
        distancia -= ener

    if ener == 0 or ener + soma_med < distancia:
        continue

    if inicio[0] != 0 and matriz[inicio[0] - 1][inicio[1]] != "#":
        fila.append((inicio[0] - 1, inicio[1], ener - 1))
        if inicio[0] != 0 and matriz[inicio[0] - 1][inicio[1]] == "T":
            print("Yes")
            exit()

    if inicio[0] < len(matriz) - 1 and matriz[inicio[0] + 1][inicio[1]] != "#":
        fila.append((inicio[0] + 1, inicio[1], ener - 1))
        if inicio[0] < len(matriz) - 1 and matriz[inicio[0] + 1][inicio[1]] == "T":
            print("Yes")
            exit()

    if inicio[1] != 0 and matriz[inicio[0]][inicio[1] - 1] != "#":
        fila.append((inicio[0], inicio[1] - 1, ener - 1))
        if inicio[1] != 0 and matriz[inicio[0]][inicio[1] - 1] == "T":
            print("Yes")
            exit()

    if inicio[1] < len(matriz[0]) - 1 and matriz[inicio[0]][inicio[1] + 1] != "#":
        fila.append((inicio[0], inicio[1] + 1, ener - 1))
        if inicio[1] < len(matriz[0]) - 1 and matriz[inicio[0]][inicio[1] + 1] == "T":
            print("Yes")
            exit()


print(result)
# dfs((xStart,yStart), e-1)
# dfs(nextX, nextY, e)
