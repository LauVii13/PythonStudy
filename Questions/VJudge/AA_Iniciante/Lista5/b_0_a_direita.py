t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == 0 or b == 0:
        print(a**b)
        continue

    lista = []

    i = 1
    while True:
        unid = (a**i) % 10
        if not unid in lista:
            lista.append(unid)
            i += 1
        else:
            i -= 1
            break

    loops = (b - 1) % i

    print(lista[loops])
