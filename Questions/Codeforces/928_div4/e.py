t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    impar = n // 2 if n % 2 == 0 else n // 2 + 1

    valor = 0
    if k <= impar:
        cont = 0
        while cont < k:
            valor = (cont * 2) + 1
            cont += 1

    else:
        lista = []
        lista.append(0)
        for i in range(2, n + 1, 2):
            lista.append(i)

        mult = 2
        cont = impar
        i = 0
        while cont < k:
            if i * 2 < len(lista) and ((i * 2 + 1) * mult // 2) < len(lista):
                if (i * 2 + 1) * mult == lista[((i * 2 + 1) * mult // 2)]:
                    valor = lista[((i * 2 + 1) * mult // 2)]
                    lista[((i * 2 + 1) * mult // 2)] = 0
                    i += 1
                else:
                    cont -= 1
            else:
                i = 0
                mult += 2
                cont -= 1

            cont += 1
    print(valor)
