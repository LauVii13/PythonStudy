def busca_indice(lista, busca):
    i, j = 0, len(lista) - 1

    if j <= 0:
        return len(lista)

    while i <= j:
        v = (i + j) // 2
        if lista[v][0] <= busca:
            i = v + 1
        else:
            j = v - 1
    return i


t = int(input())

for _ in range(t):
    n = int(input())

    lista = []

    for i in range(n):
        aluno = tuple(map(int, input().split()))

        # busca bin
        pos = busca_indice(lista, aluno[0])
        lista.insert(pos, aluno)

    seg = 0
    i = 0
    while i < len(lista):
        seg += 1
        if seg < lista[i][0]:
            continue
        elif seg > lista[i][1]:
            print(0, end=" ")
            seg -= 1
        elif seg >= lista[i][0]:
            print(seg, end=" ")

        i += 1
    print()
