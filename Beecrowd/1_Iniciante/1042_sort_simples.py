lista = [int(x) for x in input().split()]

n = lista.copy()

n.sort()

for e in n:
    print(e)

print("")

for e in lista:
    print(e)