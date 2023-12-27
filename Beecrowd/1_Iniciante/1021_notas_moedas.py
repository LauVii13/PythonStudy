total = float(input())

notas = 0

valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05]

print("NOTAS:")
for n in valores:
    notas = int(total // n)
    if n > 1:
        print(f"{notas} nota(s) de R$ {n:.2f}")
    else:
        if n == 1:
            print("MOEDAS:")
        print(f"{notas} moeda(s) de R$ {n:.2f}")
    total -= notas * n

print(f"{total * 100:.0f} moeda(s) de R$ 0.01")
