codigo, total = input().split()
cardapio = [4, 4.50, 5, 2, 1.50]

print(f"Total: R$ {cardapio[int(codigo) - 1] * int(total):.2f}")
