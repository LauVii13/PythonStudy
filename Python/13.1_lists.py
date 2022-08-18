# looping through a list works like getting characters from a string
n = ['a', 'b', 'c', 'd', 'e']

# So to extract a specific value or group of values ​​from a list use: [number1 : number2], it returns the respective index except the value number2
print(n[0:3])    # Return the index (0, 1, 2)
print(n[2:4])    # Return the index (2, 3)
print(n[2:])     # Return the index (2, 3, 4, ...)
print(n[:5])     # Return the index (0, 1, 2, 3, 4, 5)
print(n[1:-1])   # Return the index (1, 2, 3, 4, ..., respective index of -1)

n[1 : 4] = 'B', 'C', 'D'    # It's possible to change a value of a list whenever you need with this syntax
print(n)

# =====================================================================================================================================================================#

# Exercise: Write a program to find the largest number in a list

numbers = [1, 10, 4, 6, 8, 25, 3, 32, 24]
x = numbers[0]

for i in numbers:
    if x <= i:
        x = i
print(x)

# =====================================================================================================================================================================#

# You can unpacking a list, as in the example below

a, b, c, d, e, f, g, h, i = numbers
print(a, b, c, d, e, f, g, h, i)