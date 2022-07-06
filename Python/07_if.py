# if it's hot 
#     It's a hot day
#     Drink plenty of water 

# otherwise if it's cold
#     It's a cold day
#     Wear warm clothes

# otherwise
#     It's a lovely day

#=====================================================================================================================================================================#

# is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
    
# print("Enjoy your day")

#=====================================================================================================================================================================#
# Exercise:
#     Price of a house is $1M
#     if buyer has good credit, 
#         they need to put down 10%
#     otherwise
#         they need to put down 20%
    
#     print the down payment

price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: ${down_payment}")