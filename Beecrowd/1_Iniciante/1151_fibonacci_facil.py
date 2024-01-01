n = int(input())
fib0 = 0
fib1 = 1

for i in range(n - 1):
    print(fib0, end=" ")
    fib0, fib1 = fib1, fib0 + fib1

print(fib0)
