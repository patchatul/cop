month = (input("Enter month: "))
day = (input("Enter day: "))
year = (input("Enter year: "))

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

def DetermineInvalidMonthFromDay(month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if ((int(year)% 4) ==0):
        days[1]=29
    return days[int(month)-1]
MAX_DAY =DetermineInvalidMonthFromDay(month)

if int(year) <= MIN_YEAR: # invalid year
  validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
  validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
  validDate = False

if validDate == True:
      print(f"{month}/{day}/{year} is a valid date.")
else:
      print(f"{month}/{day}/{year} is an invalid date.")