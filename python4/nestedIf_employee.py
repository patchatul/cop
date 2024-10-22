name = input("enter employee's name: ")
numShifts = int(input("enter number of shifts: "))
numTransactions = int(input("enter number of transactions: "))
transactionsDollarValue = float(input("enter transaction dollar value: "))
#calculate productivityScore and get bonus
productivityScore = (transactionsDollarValue / numTransactions) /numShifts
bonus = 0.00

if productivityScore <=30:
    bonus += 50.00
elif productivityScore >=30 and productivityScore <= 69:
    bonus += 75.00
elif productivityScore >=70 and productivityScore <= 199:
    bonus += 100.00
elif productivityScore >=200:
    bonus += 200.00
    
print("Employee name: " + name)
print("Employee Bonus: $" + str(bonus))