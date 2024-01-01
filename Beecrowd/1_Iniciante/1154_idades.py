lista = []
while True:
    lista.append(int(input()))

    if lista[-1] < 0:
        break

lista.pop()

tot = sum(lista)
media = tot / len(lista)

print(f"{media:.2f}")
