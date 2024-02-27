n = int(input())
lista = list(map(int, input().split()))
lista.sort()

metade = sum(lista) // 2

cont = 0
qtd_moedas = 0

for i in range(len(lista) - 1, -1, -1):
    cont += lista[i]
    qtd_moedas += 1

    if cont > metade:
        break

print(qtd_moedas)
