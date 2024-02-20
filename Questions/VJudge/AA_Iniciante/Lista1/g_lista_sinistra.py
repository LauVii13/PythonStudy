t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    lista = list(map(int, input().split()))
    aux = list(map(lambda x: 1, lista))

    i = 0
    while True:
        if lista[i] % x != 0:
            break
        lista.append(lista[i] // x)
        aux.append(aux[i] * x)

        i += 1

    soma = sum(lista[i] * aux[i] for i in range(len(lista)))

    print(int(soma))
