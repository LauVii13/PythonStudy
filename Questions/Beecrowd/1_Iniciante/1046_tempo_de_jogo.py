ini, fim = [int(i) for i in input().split()]

if ini == fim:
    h = 24
elif ini > fim:
    h = 24 - ini
    h += fim
else:
    h = fim - ini

print(f"O JOGO DUROU {h} HORA(S)")