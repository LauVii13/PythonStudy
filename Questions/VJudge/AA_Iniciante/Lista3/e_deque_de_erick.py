n, q = map(int, input().split())
lista = list(map(int, input().split()))

bases = {}

for i in range(1, n):
    bases[i] = [lista[0], lista[1]]
    if lista[0] > lista[1]:
        lista.append(lista[1])
        lista.pop(1)
    else:
        lista.append(lista[0])
        lista.pop(0)

maior = lista[0]
lista.pop(0)

for _ in range(q):
    teste = int(input())

    if teste < n:
        par = bases[teste]
    else:
        i = teste % (n - 1)
        par = [maior, lista[i - 1]]

    for e in par:
        print(e, end=" ")
    print()
