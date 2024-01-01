lista = [int(i) for i in input().split()]

a, n = lista[0], lista[-1]

soma = 0

if a < n:
    for i in range(0, n):
        soma += i + a
else:
    for i in range(n - 1, -1, -1):
        soma += i + a
print(soma)
