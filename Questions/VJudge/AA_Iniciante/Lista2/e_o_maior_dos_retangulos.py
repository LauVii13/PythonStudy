while True:
    lista = list(map(int, input().split()))
    if lista[0] == 0:
        break
    lista.pop(0)

    l_l = []
    l_r = []
    p_l = [-1]
    p_r = [1]

    for i in range(len(lista)):
        cont = 1
        while p_l[-1] != -1 and lista[p_l[-1]] >= lista[i]:
            cont += l_l[p_l[-1]]
            p_l.pop(-1)

        l_l.append(cont)
        p_l.append(i)

        cont = 1
        while p_r[-1] != 1 and lista[p_r[-1]] >= lista[-i - 1]:
            cont += l_r[-(p_r[-1]) - 1]
            p_r.pop(-1)

        l_r.append(cont)
        p_r.append(-i - 1)

    maior = 0

    for i in range(len(l_l)):
        area = (l_l[i] + l_r[-i - 1] - 1) * lista[i]

        if area > maior:
            maior = area

    print(maior)
