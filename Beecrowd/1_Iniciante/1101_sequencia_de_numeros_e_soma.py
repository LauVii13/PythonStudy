while True:
    m, n = [int(i) for i in input().split()]
    
    if m <= 0 or n <= 0: break
    
    if m > n:
        m, n = n, m
    
    soma = 0
    for v in range(m, n + 1):
        soma += v
        print(f"{v} ", end="")
    print(f"Sum={soma}")
    