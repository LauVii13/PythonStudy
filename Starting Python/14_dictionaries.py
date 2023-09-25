# Dictionaries are used in situations where we want to store a information that comes as key value pairs.

# Imagine than you want to store a costumer's information, like 'Name' = 'John'
#                                                               'Email' = 'jh@gmai.com'
#                                                               'Phone' = '12345'
# so, to define a dictionary, we use {}

costumer = {
    'name' : 'John',
    'age' : 30,
    #'age' : 40, -> it's wrong
    'is_verified': True
}

# each key should be unique in a dictionary, we can't repeat a key, as 'age'

print(costumer['name']) # if you type 'Name' instead 'name', or some key does not exist, it'll return an error message
print(costumer.get('email')) # but with a 'get' method, instead an error message, it'll return 'None'
print(costumer.get('email', 'jh@gmail.com')) # if the dictionary doesn't have this key, we can supply the default value

costumer['phone'] = '12345'
print(costumer['phone'])
costumer['age'] = 35 # we can also update the information stored in a key

print('')
# =====================================================================================================================================================================#

# Exercise -> read a number and translate it to words (1234 -> one two three four)

phone = input("Phone: ")

numbers = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

output = ''
for ch in phone:
    output += numbers.get(ch, '*') + ' '
print(output)