while True:
    cont = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    # Incrementa as contagens com base na posição dos dígitos
    for i in range(1, 10):
        if a > 0:
            cont[i] += max(0, (min(b, 10 * a - 1) - a + 1)) * (a // 10)
        cont[i] += max(0, (min(b, 10 * a - 1) - a + 1)) % 10

    for i in range(a, min(b, 10 * a - 1) + 1):
        for n in str(i):
            cont[int(n)] += 1

    print(f"{cont[0]} {cont[1]} {cont[2]} {cont[3]} {cont[4]} {cont[5]} {cont[6]} {cont[7]} {cont[8]} {cont[9]}")
