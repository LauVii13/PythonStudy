t = int(input())
fib = [0, 1]
for j in range(t):
    fib0 = 0
    fib1 = 1

    n = int(input())

    if len(fib) - 1 < n:
        for i in range(len(fib) - 1, n):
            fib.append(fib[i - 1] + fib[i])

    print(f"Fib({n}) = {fib[n]}")
