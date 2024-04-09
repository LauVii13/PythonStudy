def dfs(n, m):
    
    result.append(n)
    pais[n] = m
    print(pais)
    
    for i in cidades[n]:
        if pais[i] == -1:
            dfs(i, n)
            
    

    


n, m = map(int, input().split())
cidades = {i + 1: [] for i in range(n)}
pais = {i + 1: -1 for i in range(n)}
result = []

for _ in range(m):
    a, b = map(int, input().split())
    cidades[a].append(b)
    cidades[b].append(a)

visitados = set()
dfs(1, 1)

print(visitados)