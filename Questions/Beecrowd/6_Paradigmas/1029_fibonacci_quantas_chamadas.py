count = 0
prev = {}
contagem = {}


def fib(x):
    global count
    
    
    if x in prev: 
        count += contagem[x]
        return prev[x]

    if x <= 1:
        contagem[x] = 0
        prev[x] = x
        return x


    result = fib(x - 2) + fib(x - 1)

    count += 1
    prev[x] = result
    contagem[x] = contagem[x - 2] + contagem [x - 1] + 2

    return result


casos = int(input())

for i in range(casos):
    count = 0
    valor = int(input())
    result = fib(valor)
    print(f"fib({valor}) = {contagem[valor]} calls = {result}")
