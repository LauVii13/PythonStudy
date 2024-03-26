def busca_bin(valor, lista):
    i, j = 0, len(lista) - 1

    while i <= j:
        busca = (i + j) // 2

        if lista[busca] <= valor:
            i = busca + 1
        else:
            j = busca - 1
    return i


n = int(input())
lista = list(map(int, input().split()))
lista.sort()
q = int(input())

for _ in range(q):
    m = int(input())
    print(busca_bin(m, lista))
