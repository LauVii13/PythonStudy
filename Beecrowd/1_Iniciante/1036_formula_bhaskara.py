from math import sqrt


def calc_delta(a, b, c):
    return b**2 - 4 * a * c


v = [float(n) for n in input().split()]
a = v[0]
b = v[1]
c = v[2]

if calc_delta(a, b, c) < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + sqrt(calc_delta(a, b, c))) / (2 * a)
    x2 = (-b - sqrt(calc_delta(a, b, c))) / (2 * a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
