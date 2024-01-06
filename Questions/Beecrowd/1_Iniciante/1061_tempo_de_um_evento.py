d_ini = int((input().split())[1])
h_ini, min_ini, seg_ini = [int(n) for n in input().split(" : ")]

d_fim = int((input().split())[1])
h_fim, min_fim, seg_fim = [int(n) for n in input().split(" : ")]

time_ini = seg_ini + (min_ini * 60) + (h_ini * 3600) + (d_ini * 86400)
time_fim = seg_fim + (min_fim * 60) + (h_fim * 3600) + (d_fim * 86400)

tot = time_fim - time_ini

d = tot // 86400
h = (tot % 86400) // 3600
m = ((tot % 86400) % 3600) // 60
s = (((tot % 86400) % 3600) % 60)

print(f"""{d} dia(s)
{h} hora(s)
{m} minuto(s)
{s} segundo(s)""")