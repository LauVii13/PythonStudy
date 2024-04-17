n, m = map(int, input().split())

grafo = {i + 1: [] for i in range(n)}

for i in range(n):
    for j in range(n):
        if i != j:
            grafo[i + 1].append(j + 1)

for _ in range(m):
    a, b = map(int, input().split())
    grafo[b].remove(a)

for k in grafo.keys():
    visitados = [False] * (n + 1)
    valores = []

    fila = [k]

    while fila:
        atual = fila[0]
        fila.pop(0)
        valores.append(atual)

        for v in grafo[k]:
            if not visitados[v]:
                visitados[v] = True
                fila.append(v)

    if len(valores) == n:
        print(*valores)
        exit()

print("IMPOSSIBLE")
