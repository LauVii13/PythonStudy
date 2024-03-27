def busca_inicio(positions, p):
    i, j = 0, len(positions) - 1

    while i < j:
        v = (i + j) // 2
        if positions[v] == p:
            return v

        elif positions[v] > p:
            j = v
        else:
            i = v + 1
    return i


s = input()
dictionary = {}
lista = []
t = []
u = ""

for i in range(len(s)):
    lista.append(ord(s[i]) - 97)
    if dictionary.get(lista[i]) == None:
        dictionary[lista[i]] = []

    dictionary[lista[i]].append(i)

i = 0
p = 0

while p < len(lista):
    positions = dictionary.get(i)

    if positions == None:
        i += 1
        continue

    while len(t) > 0 and t[-1] <= i:
        temp = t[-1]
        t.pop(-1)
        u += chr(temp + 97)

    if positions[-1] >= p:

        v = busca_inicio(positions, p)
        for x in range(v, len(positions)):
            j = positions[x]

            while j > p:
                t.append(lista[p])
                p += 1

            u += chr(i + 97)
            p += 1

    i += 1

while len(t) > 0:
    u += chr(t[-1] + 97)
    t.pop(-1)

print(u)
