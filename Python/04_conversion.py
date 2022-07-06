birth_year = input('Birth year: ') #input always will set the variable to string, Ex.: '2005' ≠ 2005 (string ≠ integer)
print(type(birth_year))
age = 2022 - int(birth_year)
print(age)
print(type(age))
print('')


#type() -> show the type of the variable 
# Ways to convert string to: 
# integer -> int()
# float -> float()
# boolean -> bool()

#=====================================================================================================================================================================#
#Exercise: ask  a user their weight(in pounds), convert it to kilograms and print on the terminal

p_weight = input('what is your weight(lbs)? ')
p_weight = int(p_weight)
kilo = p_weight * 0.45
print(kilo)

#=====================================================================================================================================================================#
