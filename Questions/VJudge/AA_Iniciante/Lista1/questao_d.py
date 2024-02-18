t = int(input())

for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    options = [i + 1 for i in range(n)]

    i = 0
    j = n - 1
    k = 0

    while i <= j:
        ganhou = True
        busca = (j + i) // 2
        jogada = options[busca]
        p1 = 0
        p2 = n - 1

        while jogada > 0:
            while lista[p2] > jogada and p2 > p1:
                p2 -= 1

            if p2 < p1 or lista[p2] > jogada:
                ganhou = False
                break

            jogada -= 1
            p2 -= 1
            p1 += 1

        if ganhou:
            k = max(options[busca], k)
            i = busca + 1
        else:
            j = busca - 1
    if n == 1:
        if lista[0] == 1:
            k = 1
    print(k)
