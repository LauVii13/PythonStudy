n = int(input())

notas = {'R': 0, 'S': 0, 'C': 0}

for i in range(n):
    num, cobaia = input().split()
    num = int(num)
    
    notas[cobaia] += num

tot = notas['R'] + notas['S'] + notas['C']

print(f"Total: {tot} cobaias")
print(f"""Total de coelhos: {notas['C']}
Total de ratos: {notas['R']}
Total de sapos: {notas['S']}""")

pc = (notas['C'] / tot) * 100
pr = (notas['R'] / tot) * 100
ps = (notas['S'] / tot) * 100

print(f"""Percentual de coelhos: {pc:.2f} %
Percentual de ratos: {pr:.2f} %
Percentual de sapos: {ps:.2f} %""")