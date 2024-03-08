from queue import PriorityQueue

t = int(input())

for _ in range(t):
    n = int(input())

    pq = PriorityQueue()
    lista = list(map(int, input().split()))

    for i in range(n):
        pq.put((-lista[i], i + 1))

    cont = 0
    resposta = []

    while not pq.empty() and pq.qsize() > 1:
        num1, id1 = pq.get()
        num2, id2 = pq.get()

        if num1 == 0 and num2 == 0:
            continue
        if num1 == 0:
            pq.put((num2, id2))
            continue
        if num2 == 0:
            pq.put((num1, id1))
            continue

        num1 += 1
        num2 += 1
        cont += 1

        pq.put((num1, id1))
        pq.put((num2, id2))

        resposta.append([id1, id2])

    print(cont)
    for v in resposta:
        print(v[0], v[1])
