s = input()
t = input()

matriz = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

a = 0
for i in range(0, len(t)):
    for j in range(0, len(s)):

        if t[i] == s[j]:
            matriz[i + 1][j + 1] = matriz[i][j] + 1
        else:
            matriz[i + 1][j + 1] = max(matriz[i + 1][j], matriz[i][j + 1])

i, j = len(t), len(s)
palavra = ""
while i > 0 and j > 0:
    if matriz[i - 1][j] == matriz[i][j - 1]:
        if matriz[i][j] != matriz[i - 1][j - 1]:
            palavra += s[j - 1]
        i -= 1
        j -= 1
    else:
        if matriz[i - 1][j] > matriz[i][j - 1]:
            i -= 1
        else:
            j -= 1
print(palavra[::-1])
