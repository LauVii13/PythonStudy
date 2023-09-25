tempo = int(input())

horas = tempo // (60 * 60)
tempo -= horas * (60 * 60)

minutos = tempo // 60
tempo -= minutos * 60

segundos = tempo

print(f"{horas}:{minutos}:{segundos}")
