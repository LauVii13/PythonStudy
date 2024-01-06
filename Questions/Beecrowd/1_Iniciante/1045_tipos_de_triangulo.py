n = [float(n) for n in input().split()]

n.sort(reverse=True)

if n[0] >= n[1] + n[2]:
    print("NAO FORMA TRIANGULO")
else:
    if n[0] ** 2 == (n[1] ** 2) + (n[2] ** 2):
        print("TRIANGULO RETANGULO")
    
    if n[0] ** 2 > (n[1] ** 2) + (n[2] ** 2):
        print("TRIANGULO OBTUSANGULO")
    
    if n[0] ** 2 < (n[1] ** 2) + (n[2] ** 2):
        print("TRIANGULO ACUTANGULO")
    
    if n[0] == n[1] and n[1] == n[2]:
        print("TRIANGULO EQUILATERO")
    
    elif (n[0] == n[1] and n[0] != n[2]) or (n[1] == n[2] and n[1] != n[0]) or (n[0] == n[2] and n[0] != n[1]):
        print("TRIANGULO ISOSCELES")