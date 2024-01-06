n = int(input())

for i in range(n):
    x, y = [float(i) for i in input().split()]
    
    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{(x / y):.1f}")