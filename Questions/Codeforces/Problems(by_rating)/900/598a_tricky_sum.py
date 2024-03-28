pot = [1]
acum = [1]
x = 1
while x * 2 < 1000000001:
    x *= 2
    pot.append(x)
    acum.append(acum[-1] + x)

for _ in range(int(input())):
    n = int(input())
    soma_n = ((1 + n) * n) // 2

    p = acum[-1]
    for i in range(len(pot)):
        if pot[i] > n:
            p = acum[i - 1]
            break
    soma_n -= p * 2
    print(soma_n)
