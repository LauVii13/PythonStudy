n = int(input())
lista = list(map(int, input().split()))

somatoria = list(map(lambda x: 0, lista))
somatoria[0] = lista[0]

for i in range(1, len(lista)):
    if lista[i] + somatoria[i - 1] > lista[i]:
        somatoria[i] = lista[i] + somatoria[i - 1]
    else:
        somatoria[i] = lista[i]

print(max(somatoria))
