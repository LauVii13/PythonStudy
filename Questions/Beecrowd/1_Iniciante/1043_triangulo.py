a, b, c = [float(x) for x in input().split()]

if a < b + c and b < a + c and c < a + b:
    perim = a + b + c
    print(f"Perimetro = {perim:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")