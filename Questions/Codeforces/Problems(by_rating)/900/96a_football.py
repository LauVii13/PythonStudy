lista = list(map(lambda x: int(x), input()))

cont = 1
for i in range(1, len(lista)):
    if lista[i] == lista[i - 1]:
        cont += 1
    else:
        cont = 1

    if cont >= 7:
        break

if cont >= 7:
    print("YES")
else:
    print("NO")
