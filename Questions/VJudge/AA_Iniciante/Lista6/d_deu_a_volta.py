def volta(x, e, pais, resposta1, resposta2):
    while True:
        v1, v2 = x, e
        resposta1.append(v1)
        resposta2.append(v2)

        if x == e:
            break
        x = pais[x]
        e = pais[e]


n, m = map(int, input().split())
cidades = {i + 1: [] for i in range(n)}
pais = {i + 1: -1 for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    cidades[a].append(b)
    cidades[b].append(a)

# print(cidades)
fila = [1]
pais[1] = 1

resposta1 = []
resposta2 = []

while fila:
    x = fila[0]
    fila.pop(0)
    for e in cidades[x]:
        if pais[e] == -1:
            pais[e] = x
            fila.append(e)
        elif e == pais[x]:
            continue
        elif pais[e] != x:
            volta(x, e, pais, resposta1, resposta2)
            break
    if len(resposta1) + len(resposta2) >= 4:
        break
    else:
        resposta1 = []
        resposta2 = []

resposta1.reverse()
r = resposta1 + resposta2
if r[0] == r[1]:
    r.pop(0)
if r[-1] == r[-2]:
    r.pop(-1)

if len(r) < 4:
    print("IMPOSSÍVEL")
else:

    resp = ""
    print(len(r))
    for i in range(len(r) - 1):
        resp += f"{r[i]} "
    resp += f"{r[-1]}"
    print(resp)
