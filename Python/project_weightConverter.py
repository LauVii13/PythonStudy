from lib2to3.pytree import convert


weight = float(input('Weight: '))
i = input('(L)bs or (K)g: ')



if i.upper() == 'L':
    n = weight / 2.2
    print(f"You are {round(n, 2)} kilos")
    
elif i.upper() == 'K':
    n = weight * 2.2
    print(f"You are {round(n, 2)} pounds")
    
else:
    print("You didn't type the values ​​correctly")