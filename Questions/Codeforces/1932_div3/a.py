t = int(input())

for _ in range(t):
    n = int(input())
    lista = [i for i in input()]

    cont = 0
    i = 0
    while i < len(lista) - 1:

        if lista[i + 1] != "*":
            i += 1
        elif i < len(lista) - 2 and lista[i + 2] != "*":
            i += 2
        else:
            break

        if lista[i] == "@":
            cont += 1

    print(cont)
