n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num_zeros_b = b.count(0)

b = [elem for elem in b if elem != 0]

num_zeros_a = min(num_zeros_b, a.count(0))
for i in range(num_zeros_a):
    a.pop(a.index(0))


resposta = 0
mudou = False
for i in range(len(b)):
    menor = (b[i] - (a[0] % m) + m) % m
    mj = 0
    for j in range(1, len(a)):
        x = (b[i] - (a[j] % m) + m) % m
        if x < menor:
            menor = x
            mj = j

    if menor > resposta:
        resposta = menor

    a.pop(mj)


print(resposta)
