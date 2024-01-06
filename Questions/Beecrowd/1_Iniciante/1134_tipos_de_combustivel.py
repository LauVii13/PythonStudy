types = {1: 0, 2:0, 3:0}
while True:
    n = int(input())
    
    if n == 4: break

    if n == 1 or n == 2 or n == 3:
        types[n] += 1
    
    
print(f"""MUITO OBRIGADO
Alcool: {types[1]}
Gasolina: {types[2]}
Diesel: {types[3]}""")