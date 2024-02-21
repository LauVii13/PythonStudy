n = int(input())

cont = 0
for _ in range(n):
    op = input()

    if "++" in op:
        cont += 1
    else:
        cont -= 1
print(cont)
