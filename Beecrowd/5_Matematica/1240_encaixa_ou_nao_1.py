qtd = int(input())

for i in range(qtd):
    encaixa = True
    a, b = input().split()

    if len(a) >= len(b):
      for v in range(-1, -len(b)-1, -1):
        if b[v] != a[v]:
            encaixa = False
            break
    else:
      encaixa = False
      
    if encaixa:
        print("encaixa")
    else:
        print("nao encaixa")

