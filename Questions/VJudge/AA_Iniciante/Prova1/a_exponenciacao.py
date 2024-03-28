def verifica(a, b, c):
    if c % 2 == 0:
        if a < 0:
            a *= -1
        if b < 0:
            b *= -1        
            
    if a == b:
        return "="
    if a < b:
        return "<"
    if a > b:
        return ">"

a, b, c = map(int, input().split())

print(verifica(a, b, c))