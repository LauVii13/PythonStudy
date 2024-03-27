import heapq

t = int(input())

for _ in range(t):
    n = int(input())

    # Usando uma lista para simular a fila de prioridade
    pq = []
    lista = list(map(int, input().split()))

    for i in range(n):
        # Adicionando elementos à lista com o negativo do valor para
        # simular uma fila de prioridade máxima
        heapq.heappush(pq, (-lista[i], i + 1))

    cont = 0
    resposta = []

    while len(pq) > 1:
        num1, id1 = heapq.heappop(pq)
        num2, id2 = heapq.heappop(pq)

        if num1 == 0 and num2 == 0:
            continue
        if num1 == 0:
            heapq.heappush(pq, (num2, id2))
            continue
        if num2 == 0:
            heapq.heappush(pq, (num1, id1))
            continue

        num1 += 1
        num2 += 1
        cont += 1

        heapq.heappush(pq, (num1, id1))
        heapq.heappush(pq, (num2, id2))

        resposta.append([id1, id2])

    print(cont)
    for v in resposta:
        print(v[0], v[1])
