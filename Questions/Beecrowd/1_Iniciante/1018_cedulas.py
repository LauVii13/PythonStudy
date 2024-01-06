total = int(input())
print(total)

notas = 0

valores = [100, 50, 20, 10, 5, 2, 1]

for n in valores:
    notas = total // n
    print(f"{notas} nota(s) de R$ {n},00")
    total -= notas * n
