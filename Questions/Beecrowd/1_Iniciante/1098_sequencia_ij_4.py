i = 0
j = [1, 2, 3]

for n in range(11):
    for v in range(3):
        
        if i == 0.0 or i == 1.0 or i > 1.9:
             print(f"I={i:.0f} J={j[v] + i:.0f}")
        else:
            print(f"I={i:.1f} J={j[v] + i:.1f}")   
    i += 0.2