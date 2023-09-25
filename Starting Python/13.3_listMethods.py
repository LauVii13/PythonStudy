# Some operations that you can perform in a list -> list functions

numbers = [4, 6, 1, 5, 2, 3]

numbers2 = numbers.copy()   # copy the list to a new variable, like a backup
numbers.append(7)           # add the value to the end of the list
numbers.insert(6, 1)        # add the value 1 at the index 6
numbers.remove(1)           # remove the first specified value (in this case, the value 1 in the index 2)
numbers.pop(4)              # remove a value by the index (remove the value with index 4 -> (5) )
print(numbers.index(6))     # search the index of the item (item 6 -> index = 1)
numbers.sort()              # sort the items in ascending order
numbers.reverse()           # reverse the list, the first item becomes the last and vice versa

print (numbers)
print(41 in numbers)        # true if 41 exist in the list and false if not  
print (numbers.count(2))    # print how many times the item repeat   
 
numbers.clear()            # delete all items

print('')

# =====================================================================================================================================================================#

# Exercise: write a program to remove the duplicates in a list

n = [2, 2, 5, 3, 1, 5, 4, 2, 1]
li= []

for i in n:
    if i not in li:
        li.append(i)

li.sort()
print(li)
