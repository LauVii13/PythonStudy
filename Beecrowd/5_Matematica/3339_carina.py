import math

qtd = int(input())

for i in range(qtd):
  a, b = input().split()
  a, b = int(a), int(b)

  a2 = math.ceil(math.sqrt(a))
  b2 = math.floor(math.sqrt(b))

  print(b2 - a2 + 1)