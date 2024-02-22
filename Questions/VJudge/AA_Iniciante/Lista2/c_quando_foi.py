n, q = map(int, input().split())
lista = list(map(int, input().split()))
ocorr = {}

for i in range(n):
    if ocorr.get(lista[i]):
        ocorr[lista[i]].append(i)
    else:
        ocorr[lista[i]] = [i]

for _ in range(q):
    x, k = map(int, input().split())
    valor = -1

    if ocorr.get(x) and k <= len(ocorr[x]):
        valor = ocorr[x][k - 1]
        valor += 1

    print(valor)
