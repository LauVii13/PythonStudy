l = [i for i in input()]
mod = int(1e9 + 7)

tot_a = 0
soma = 0
i = 1
for n in l:
    if n == "a":
        i = (i * 2) % mod
    else:
        soma = (soma + i - 1) % mod

print(soma)
