def crivoEratostenes(n):
    elemento = [True for _ in range(n + 1)]

    elemento[0], elemento[1] = False, False

    primos = []

    for num, primo in enumerate(elemento):
        if primo:
            primos.append(num)
            print(num)

            for i in range(pow(num, 2), n + 1, num):
                elemento[i] = False

    return primos


n = pow(2, 25)
print("--------")
crivoEratostenes(n)
print("--------")
