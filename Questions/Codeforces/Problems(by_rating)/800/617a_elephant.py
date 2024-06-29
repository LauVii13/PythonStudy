n = int(input())

cont = 0
for i in range(5, 0, -1):
    cont += n // i
    n = n % i
print(cont)
