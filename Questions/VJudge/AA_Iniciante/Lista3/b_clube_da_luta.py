# wa - questao nao resolvida
def buscabin(lista, k):
    i = 0
    j = len(lista) - 1
    while i < j:
        p = (j + i) // 2
        if lista[p] == k:
            return p

        if lista[p] < k:
            i = p + 1
        else:
            j = p - 1
    return i


t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    lista = list(map(int, input().split()))
    listai = []

    for i in range(n):
        listai.append((lista[i], i))

    dictionary = {}

    a = listai[0]
    dictionary[a[1]] = [0]

    for i in range(1, n):
        b = listai[i]

        if dictionary.get(b[1]) == None:
            dictionary[b[1]] = [0]

        if a[0] > b[0]:
            vd = dictionary[a[1]]
            vd[0] += 1
            vd.append(i)

            dictionary[a[1]] = vd
        else:
            vd = dictionary[b[1]]
            vd[0] += 1
            vd.append(i)

            dictionary[b[1]] = vd
            a = b

    for _ in range(q):
        i, k = map(int, input().split())

        if i - 1 != a[1]:
            valor = dictionary[i - 1]
            print(valor[0])
        else:
            if k >= n:
                valor = dictionary[a[1]]
                print(valor[0] + (k - (n - 1)))
            else:
                turnos = dictionary[a[1]]
                cont = turnos.pop(0)
                cont -= len(turnos) - buscabin(turnos, k) - 1
                print(cont)
