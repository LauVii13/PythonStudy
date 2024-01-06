inter = 0
gremio = 0
emp = 0

while True:
    a, b = [int(i) for i in input().split()]
    
    if a > b:
        inter += 1
    elif a < b:
        gremio += 1
    else:
        emp += 1
    
    print("Novo grenal (1-sim 2-nao)")
    
    op = int(input())
    
    if op == 2: break

print(f"""{inter + gremio + emp} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{emp}""")

if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")