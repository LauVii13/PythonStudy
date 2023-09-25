course = 'Python for Beginners'

#if you want to use ' in your string, like (Python's course for beginners), you will need to use ""  instead of '' (example 1), and vice versa (example 2)

course = "Python's Course for Beginners" #example 1
course = 'Python for "Beginners"' #example 2

#and if you need to write a string with multiple lengths, you'll use ''' (text) '''

course = '''
Hi, my nickname is LauVii,
And this is an example of a string with two or more lines.

Bye!
'''

#Going back to the first line example...

course = 'Python for Beginners' #Python strings are indexed and using [(number)] you can get the respective character
   #index:012345
print(course[0]) #return P

#using a negative value, it will return the character starting the count from the end
print(course[-2]) #return r

#to extract a few characters use: [number1 : number2], it returns the respective index except the number2 character
print(course[0:3]) #return Pyt -> return the index (0, 1, 2)
print(course[2:4]) #return Pyt -> return the index (2, 3)
print(course[2:]) #return Pyt -> return the index (2, 3, 4, ...)
print(course[:6]) #return Pyt -> return the index (0, 1, 2, 3, 4, 5)
print(course[1:-1]) #return Pyt -> return the index (1, 2, 3, 4, ..., respective index of -1)


