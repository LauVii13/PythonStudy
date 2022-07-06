# if temperature is greater then 30
#     it's a hot day
# otherwise if it's less than 10
#     it's a cold day
# otherwise
#     it's neither hot nor cold


temperature = 30

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")
    
    
# COMPARISON OPERATORS
# ---------------------------------
# > -> greater than
# < -> less than
# >= -> greater than or equal to
# <= -> less than or equal to
# == -> equals to
# != -> not equal to
# ---------------------------------
# Exercise:
# If name is less than 3 characters long
#   print -> name must be at least 3 characters
# Otherwise if it's more than 50 characters long
#   print -> name can be a maximum of 50 characters
# Otherwise 
#   print -> name looks good!

name = input('Type your name: ')

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
