n, q = map(int, input().split())

valores = list(map(int, input().split()))
valores.insert(0, 0)
somatoria = list(map(lambda x: 0, valores))
somatoria[0] = valores[0]

for i in range(1, len(valores)):
    somatoria[i] = valores[i] + somatoria[i - 1]

for _ in range(q):
    a, b = map(int, input().split())
    print(somatoria[b] - somatoria[a - 1])
