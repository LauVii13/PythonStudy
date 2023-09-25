first = 'John'
last = 'Smith'

#we want to print the phrase: John [Smith] is a coder
message = first + ' [' + last + '] is a coder'

#formatted string -> without the + to concatenate, it is a way of simplifying the last example
msg = f'{first} [{last}] is a coder'
print(msg)