salary = float(input("Enter Salary :"))
numDependents = float(input("Enter Number of Dependents :"))
#calculate tax
stateTax = salary * (6.5/100)
federalTax = salary * (28.0/100)
dependentDeduction = (salary * (2.5/100)) * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding


print(f"State Tax: ${stateTax:.2f}") 
print(f"Federal Tax: ${federalTax:.2f}") 
print(f"Dependent Deduction: ${dependentDeduction:.2f}") 
print(f"Salary: ${salary:.2f}") 
print(f"Take Home Pay: ${takeHomePay:.2f}")
'''
print("State Tax: $" +  str(stateTax))
print("Federal Tax: $" +  str(federalTax))
print("Dependent Deduction: $" +  str(dependentDeduction))
print("Salary: $" +  str(salary))
print("Take Home Pay: $" + str(takeHomePay))
'''