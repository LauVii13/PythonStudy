n, k = map(int, input().split())
quarto = [int(i) for i in input()]

vaga = []

for i in range(n):
    if quarto[i] == 0:
        vaga.append(i)

p1 = 0
p2 = k
t = 1

maior = max(vaga[t] - vaga[p1], vaga[p2] - vaga[t])
fim = maior
while p2 < len(vaga):

    while t < p2 - 1 and max(vaga[t + 1] - vaga[p1], vaga[p2] - vaga[t + 1]) < max(
        vaga[t] - vaga[p1], vaga[p2] - vaga[t]
    ):
        t += 1

    maior = max(vaga[t] - vaga[p1], vaga[p2] - vaga[t])
    fim = min(maior, fim)
    p1 += 1
    p2 += 1
    if p1 == t:
        t += 1

print(fim)
