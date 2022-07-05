course = 'Python for Beginners'
len(course) #count the size of the variable, if it's a string, count the number of characters

#method ≠ function
#method is a type of function, specific to an object, in this case, upper is a method to string 
#functions have a general porpouse, they don't belong to an especific group 

print(course.upper()) #convert the string into upper case
print(course.lower()) #convert the string into lower case
print(course.find('t')) #return the index of the first accurrence of that character (case sensitive)
print(course.replace('Python', 'Java')) #replace a character or a sequence of characters(replace the first term by the second)
print('Python' in course) #checks if the term is in the variable -> return True or False
print(course.title()) #convert the first character of the word into upper case