t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    degrau = list(map(int, input().split()))
    teste = list(map(int, input().split()))
    degrau.insert(0, 0)
    minimo = [degrau[0]]

    for i in range(1, len(degrau)):
        minimo.append(max(minimo[i - 1], degrau[i]))
        degrau[i] += degrau[i - 1]

    for i in range(q):
        p1 = 0
        p2 = len(minimo) - 1
        maior = 0
        while p1 <= p2:
            k = (p2 + p1) // 2
            if minimo[k] <= teste[i]:
                if minimo[k] > minimo[maior]:
                    maior = k
                if minimo[k] == minimo[maior] and k > maior:
                    maior = k
                p1 = k + 1
            else:
                p2 = k - 1
        print(degrau[maior], end=" ")
    print()
