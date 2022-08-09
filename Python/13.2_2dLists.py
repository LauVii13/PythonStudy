# A 2D list looks like a matrix in math, so a 2d list can be made using lists inside a main one

main = [
    [1, 2, 3, 4],  # this list is equivalent to main[0]
    [5, 6, 7, 8]   # and this to main[1]
] 

# If you want to access the value 7 for example, you just need to type main[1][2] 
# print(main[1][2])

for x in main:
    print(x)
    for i in x:
        print(i)