a, b = map(int, input().split())
lista = []
while True:
    if a >= b:
        break

    if b % 2 == 0:
        lista.append(b)
        b //= 2

    elif b % 10 == 1:
        lista.append(b)
        b //= 10
    else:
        break

lista.append(b)
if b == a:
    print("YES")
    print(len(lista))
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i], end=" ")
else:
    print("NO")
