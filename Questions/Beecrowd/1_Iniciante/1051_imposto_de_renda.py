salary = float(input())

if salary <= 2000.00:
    print("Isento")
else:
    if salary > 2000.00 and salary <= 3000.00:
        value = (salary - 2000) * 0.08
    elif salary > 3000.00 and salary <= 4500.00:
        value = ((salary - 3000) * 0.18) + (1000 * 0.08)
    else:
        value = (salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
        
    print(f"R$ {value:.2f}")