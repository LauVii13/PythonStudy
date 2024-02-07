def verificaFrase(lista, n, x, cont):
    if n == 1:
        if lista[0] != x:
            cont += 1
        return cont

    n = round(n / 2)
    if lista[:n].count(x) > lista[n:].count(x):
        cont += n - lista[:n].count(x)
        nova_lista = lista[n:]
    elif lista[:n].count(x) < lista[n:].count(x):
        cont += n - lista[n:].count(x)
        nova_lista = lista[:n]
    else:
        cont_parcial1 = verificaFrase(lista[:n], n, x + 1, 0)
        cont_parcial2 = verificaFrase(lista[n:], n, x + 1, 0)

        if cont_parcial1 == cont_parcial2:
            cont += n - lista[n:].count(x)
            nova_lista = lista[:n]
        elif cont_parcial1 < cont_parcial2:
            cont += n - lista[n:].count(x)
            nova_lista = lista[:n]
        else:
            cont += n - lista[:n].count(x)
            nova_lista = lista[n:]

    return verificaFrase(nova_lista, n, x + 1, cont)


t = int(input())

for _ in range(t):
    n = int(input())
    frase = input()
    lista = list(map(lambda x: ord(x) - 96, frase))

    cont = 0
    x = 1

    cont = verificaFrase(lista, n, x, cont)

    print(cont)
