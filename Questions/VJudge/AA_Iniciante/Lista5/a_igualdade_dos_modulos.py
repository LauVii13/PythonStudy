n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

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
