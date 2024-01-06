salary = float(input())
option = 0

if salary <= 400.00:
    new_salary = salary * 1.15
    option = "15 %"
elif salary > 400.00 and salary <= 800.00:
    new_salary = salary * 1.12
    option = "12 %"
elif salary > 800.00 and salary <= 1200.00:
    new_salary = salary * 1.10
    option = "10 %"
elif salary > 1200.00 and salary <= 2000.00:
    new_salary = salary * 1.07
    option = "7 %"
else:
    new_salary = salary * 1.04
    option = "4 %"
    
print(f"Novo salario: {new_salary:.2f}")

reajuste = new_salary - salary
print(f"Reajuste ganho: {reajuste:.2f}")

print(f"Em percentual: {option}")

