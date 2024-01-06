n = int(input())
lista = list(map(int, input().split()))

lista.sort()

tot = lista.count(max(lista))

print(lista[-tot - 1])