lista = list(map(int, input().split()))

soma = 0

for _ in range(lista.count(1)):
    pos = lista.index(1)
    soma += 2 ** pos
    
    lista[pos] = 0
print(soma)