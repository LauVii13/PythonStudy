n = int(input())
lista = list(map(int, input().split()))

maior = 1
cont = 1

for i in range(n - 1):
    if lista[i] <= lista[i + 1]:
        cont += 1
    else:
        cont = 1
    maior = cont if maior < cont else maior

print(maior)
