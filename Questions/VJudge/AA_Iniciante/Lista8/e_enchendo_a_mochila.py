total, n = map(int, input().split())
lista = [0 for i in range(total + 1)]

for _ in range(n):
    peso, valor = map(int, input().split())

    for i in range(len(lista) - 1, 0, -1):
        complemento = lista[i - peso]
        if (i - peso == 0 or complemento != 0) and not i - peso < 0:
            if complemento + valor > lista[i]:
                lista[i] = complemento + valor


print(max(lista))
