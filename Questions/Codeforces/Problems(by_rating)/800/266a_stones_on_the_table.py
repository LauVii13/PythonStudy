n = int(input())
stones = [i for i in input()]

cont = 0

for i in range(n - 1, 0, -1):
    if stones[i] == stones[i - 1]:
        cont += 1

print(cont)
