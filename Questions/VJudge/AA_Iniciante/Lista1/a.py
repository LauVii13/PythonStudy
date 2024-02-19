def verificaFrase(lista, x):
    cont = 0
    n = (len(lista))
    if n == 2:
        if not(x in lista):
            cont += 1
        if not(x+1 in lista):
            cont += 1
        return cont
    
    n = n // 2
    caminho1 = n - lista[:n].count(x)
    caminho2 = n - lista[n:].count(x)
    
    filho1 = verificaFrase(lista[:n], x+1)
    filho2 = verificaFrase(lista[n:], x+1)
    
    return min(caminho1 + filho2, caminho2 + filho1)
    
    
t = int(input())

for _ in range(t):
    n = int(input())
    frase = input()
    lista = list(map(lambda x: ord(x) - 96, frase))

    cont = 0
    x = 1

    if n == 1:
        if lista[0] != x:
            cont += 1
    else:
        cont = verificaFrase(lista, x)

    print(cont)