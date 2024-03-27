t = int(input())

for _ in range(t):
    n = int(input())
    dictionary = {}

    lista = list(map(int, input().split()))

    maior = 0
    for value in lista:
        if dictionary.get(value) == None:
            dictionary[value] = 0

        dictionary[value] += 1

        if dictionary[value] > maior:
            maior = dictionary[value]

    if maior > n // 2:
        pares = n - maior
        print(n - pares * 2)
    else:
        if n % 2 == 0:
            print(0)
        else:
            print(1)
