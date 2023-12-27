a, b = [int(x) for x in input().split()]

if b > a:
    a, b = b, a

if a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")