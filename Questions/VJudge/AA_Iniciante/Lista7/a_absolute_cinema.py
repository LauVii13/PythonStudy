import heapq

n, k = map(int, input().split())

filmes = []
for _ in range(n):
    a, b = map(int, input().split())
    filmes.append((-b, -a))

filmes.sort()

tempo = [0 for _ in range(k)]
heapq.heapify(tempo)

cont = 0
indice_filmes = 0
while indice_filmes < len(filmes) and tempo:
    fim, ini = filmes[indice_filmes][0], filmes[indice_filmes][1]
    print(1, filmes, tempo)

    term = heapq.heappop(tempo)
    print(ini, fim, term)
    if ini >= term:
        term = fim
        cont += 1

    heapq.heappush(tempo, term)

    indice_filmes += 1
print(cont)
