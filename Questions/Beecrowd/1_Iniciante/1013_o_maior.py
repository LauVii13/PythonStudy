a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maior = (a + b + abs(a - b)) / 2

maior = (maior + c + abs(maior - c)) / 2
maior = int(maior)
print(f'{maior} eh o maior')