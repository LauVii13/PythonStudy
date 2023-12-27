A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

tri = A * C / 2
cir = pi * pow(C, 2)
tra = (A + B) * C / 2
qua = pow(B, 2)
ret = A * B
print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')