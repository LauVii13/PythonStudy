n = int(input())

for i in range(n):
    x, y = [int(e) for e in input().split()]

    soma = 0
    if x % 2 == 0:
        x += 1

    for j in range(y):
        soma += x
        x += 2

    print(soma)
