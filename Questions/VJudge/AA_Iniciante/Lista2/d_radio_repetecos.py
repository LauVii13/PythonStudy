n = int(input())

lista = list(map(int, input().split()))
dic = {}

p0 = 0
cont = 0
maior = 0

for i in range(n):
    if dic.get(lista[i]) != None:
        valor = dic.get(lista[i])
    else:
        valor = -1

    dic[lista[i]] = i

    if valor >= p0:
        p0 = valor + 1

    cont = i - p0 + 1

    if cont > maior:
        maior = cont
print(maior)
