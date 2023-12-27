n = [float(x) for x in input().split()]

media = ((n[0] * 2) + (n[1] * 3) + (n[2] * 4) + (n[3] * 1)) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    rec = float(input())
    print(f"Nota do exame: {rec:.1f}")
    
    media = (media + rec) / 2
    
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media:.1f}")