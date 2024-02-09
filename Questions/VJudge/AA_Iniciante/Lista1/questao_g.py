t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    lista = list(map(int, input().split()))

    extra = []
    j = 0
    fim_da_lista = True

    for v in lista:
        if v % x != 0:
            fim_da_lista = False
            break

        cont = 0
        cpv = v
        while cpv % x == 0:
            cont += 1
            cpv //= x

        extra.append(cont)

    if fim_da_lista:

        indice_menor = extra.index(min(extra))
        print(indice_menor)
        segundo_menor = (
            extra.index(min(extra[:indice_menor]))
            if len(extra) > 2 or indice_menor <= 0
            else indice_menor
        )

        for i in range(len(extra)):
            if i < indice_menor:
                extra[i] = (
                    extra[indice_menor] + 1
                    if extra[indice_menor] < extra[i]
                    else extra[indice_menor]
                )
            else:
                extra[i] = extra[indice_menor]

        print(extra)

        # while True:
        #     if extra[j] % x != 0:
        #         break
        #     extra.append([extra[j][0] // x, extra[j][1] * x])
        #     j += 1

    # soma = sum(item[0] * item[1] for item in extra) + sum(lista)

    # print(int(soma))
