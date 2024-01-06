t = int(input())

for j in range(t):
    dados = [float(i) for i in input().split()]

    count = 0
    while True:
        dados[0] += (dados[0] * (dados[2] / 100)) // 1
        dados[1] += (dados[1] * (dados[3] / 100)) // 1

        count += 1

        if dados[0] > dados[1] or count > 100:
            break

    if count > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{count} anos.")
