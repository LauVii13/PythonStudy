t = int(input())

for _ in range(t):
    cont = []
    n = int(input())
    for i in range(n):
        lista = [int(j) for j in input()]
        if lista.count(1) > 0:
            cont.append(lista.count(1))

    if cont[0] == cont[1]:
        print("SQUARE")
    else:
        print("TRIANGLE")
