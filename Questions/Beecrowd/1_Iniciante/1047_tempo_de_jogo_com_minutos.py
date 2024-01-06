h_ini, m_ini, h_fim, m_fim = [int(n) for n in input().split()]

temp_ini = h_ini * 60 + m_ini
temp_fim = h_fim * 60 + m_fim

if temp_fim <= temp_ini:
    tot = (24 * 60) - temp_ini + temp_fim
else:
    tot = temp_fim - temp_ini

h = tot // 60
m = tot % 60

print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")