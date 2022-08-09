# Nested Loops looks like a loop inside another loop, it's useful to generate coordinates 
# -> (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# ...

for x in range(4): # outer loop
    for y in range(3): # insider loop
        print(f'({x}, {y})')
        
