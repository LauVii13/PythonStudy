#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

for item in 'Python':
    print(item)

print('\n')
  
#=====================================================================================================================================================================#

for item in ['Mosh', 'Anna', 'John', 'Sarah']:
    print(item)

print('\n')

#=====================================================================================================================================================================#
 
for item in [2, 3, 4]:
    print(item)
    
print('\n')

#=====================================================================================================================================================================#
 
for item in range(5, 10):
    print(item)
    
print('\n')

#=====================================================================================================================================================================#
 
for item in range(5, 10, 2):
    print(item)
    
print('\n')

#=====================================================================================================================================================================#
# Exercise: Write a program to calculate the total cost of all items in a shopping cart, using a list of prices.

prices = [10, 9.99, 18, 15]

n = 0

for i in prices:
    n += i

print(f"The total value is {n} dollars")

# =====================================================================================================================================================================#

# Challenge
# Draw that 'F' using for loop
# xxxxx
# xx
# xxxxx
# xx
# xx

numbers = [5, 2, 5, 2, 2]

for i in numbers:
    print('x' * i)