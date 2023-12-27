lista = [float(n) for n in input().split()]

media = (lista[0] * 2 + lista[1] * 3 + lista[2] * 4 + lista[3] * 1) / 10
media = float(f"{media:.1f}")
print(f"Média: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    recuperacao = float(input())
