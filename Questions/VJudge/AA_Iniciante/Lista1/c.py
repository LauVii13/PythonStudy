n, k = map(int, input().split())
elementos = list(map(int, input().split()))

pivo = 2
contador = 2

while contador < k:
    pivo += 1
    contador += pivo

pivo -= 2
ultimo = pivo
while contador != k:
    contador -= 1
    pivo -= 1

    if pivo < 0:
        pivo = ultimo

print(elementos[pivo])
