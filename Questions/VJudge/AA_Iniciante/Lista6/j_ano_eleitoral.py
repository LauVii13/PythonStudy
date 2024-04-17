def find(p):
    if cidades[p] == p:
        return p

    cidades[p] = find(cidades[p])
    return cidades[p]


def union(p, q):
    p = find(p)
    q = find(q)

    if p == q:
        return

    if tam[p] > tam[q]:
        p, q = q, p

    cidades[p] = q
    tam[q] += tam[p]


n, m = map(int, input().split())

tam = [1 for i in range(n + 1)]
tam[0] = 0
cidades = {i + 1: i + 1 for i in range(n)}

tot_grupos = n

for _ in range(m):
    cidade1, cidade2 = map(int, input().split())

    union(cidade1, cidade2)

    tot_grupos -= 1
    if tot_grupos <= 0:
        tot_grupos = 0
    maior = max(tam)

    print(tot_grupos, maior)
