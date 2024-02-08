def verificaFrase(lista, n, x, cont, taman):

    if n == 1:
        if lista[0] != x:
            cont += 1
        return cont

    n = round(n / 2)
    base1 = 0
    base2 = 0

    for e in lista[:n]:
        if (e <= taman) and (e != 1):
            base1 += 1

    for e in lista[n:]:
        if (e <= taman) and (e != 1):
            base2 += 1

    if lista[:n].count(x) == n:
        cont += n - lista[:n].count(x)
        nova_lista = lista[n:]
    elif lista[n:].count(x) == n:
        cont += n - lista[n:].count(x)
        nova_lista = lista[:n]
    elif base1 < base2:
        cont += n - lista[:n].count(x)
        nova_lista = lista[n:]
    elif base1 > base2:
        cont += n - lista[n:].count(x)
        nova_lista = lista[:n]
    else:
        cont_parcial1 = verificaFrase(lista[:n], n, x + 1, 0, taman)
        cont_parcial2 = verificaFrase(lista[n:], n, x + 1, 0, taman)

        if cont_parcial1 <= cont_parcial2:
            cont += n - lista[n:].count(x)
            nova_lista = lista[:n]
        else:
            cont += n - lista[:n].count(x)
            nova_lista = lista[n:]

    return verificaFrase(nova_lista, n, x + 1, cont, taman)


t = int(input())

for _ in range(t):
    n = int(input())
    frase = input()
    lista = list(map(lambda x: ord(x) - 96, frase))

    cont = 0
    x = 1

    cont = verificaFrase(lista, n, x, cont, n)

    print(cont)

# def teste(lista, n, x, cont):

#     print("------------------")
#     print(lista, n, x)

#     if n == 2:
#         if ((x in lista) and not (x + 1 in lista)) or (
#             not (x in lista) and (x + 1 in lista)
#         ):
#             cont += 1
#         elif not (x in lista) and not (x + 1 in lista):
#             cont += 2
#         return cont

#     n = round(n / 2)
#     caminho1 = teste(lista[:n], n, x + 1, cont)  # 2 -
#     caminho2 = teste(lista[n:], n, x + 1, cont)  # 0 -

#     if caminho1 > caminho2:
#         cont += caminho2
#     else:
#         cont += caminho1

#     print(f"caminhos: {caminho1} {caminho2} = {cont}")
#     print("------------FIM CAMINHO------------")
#     return cont


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     frase = input()
#     lista = list(map(lambda x: ord(x) - 96, frase))

#     cont = 0
#     if n == 1:
#         if lista[0] != 1:
#             cont = 1
#     elif n == 2:
#         cont = teste(lista, n, 1, 0)
#     else:
#         n = round(n / 2)
#         caminho1 = teste(lista[:n], n, 2, 0)
#         print("==============")
#         caminho2 = teste(lista[n:], n, 2, 0)
#         print("==============")
#         print(caminho1, caminho2)
#         if caminho1 < caminho2:
#             cont = caminho1
#             print(lista, cont)
#             cont += n - lista[n:].count(1)
#         else:
#             cont = caminho2
#             print(lista, cont)
#             cont += n - lista[:n].count(1)

#     print("==============FIM==============")
#     print(cont)
