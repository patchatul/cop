month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

validDate = True

if year <= 0:
    validDate = False
elif month < 1 or month > 12:
    validDate = False
elif day < 1 or day > 31:
    validDate = False

if validDate == True:
    print(str(month) +"/" + str(day) + "/" + str(year) + " is a valid date")
else:
    print(str(month) +"/" + str(day) + "/" + str(year) + " is an invalid date")