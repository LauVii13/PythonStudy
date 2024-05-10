def power_mod(a, b, m):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return pow(power_mod(a, b // 2, m), 2) % m
    else:
        return (a * power_mod(a, b - 1, m)) % m


def encript(m, key):
    e, n = key[0], key[1]
    return power_mod(m, e, n)


def decript(c, key):
    d, n = key[0], key[1]
    return power_mod(c, d, n)


p, q = 33554317, 33554393
n = p * q
tn = (p - 1) * (q - 1)
e = 98467
d = 163097906978827

# MAX 7 CARACTERES MAIUSCULOS
m = "ABCDEFG"
mascii = ""
for i in m:
    mascii += str(ord(i))


publica = (e, n)
privada = (d, n)
print("Chave pública: ", publica)

mascii = int(mascii)

c = encript(mascii, publica)
print("Mensagem criptografada: ", c)
mdec = decript(c, privada)

for i in range(0, len(str(mdec)) - 1, 2):

    e1, e2 = str(mdec)[i], str(mdec)[i + 1]
    print(chr(int(e1 + e2)), end="")
