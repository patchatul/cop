charge = 35.00

numChars = int(input("enter number of characters: "))
woodType = input("enter type of wood: ")
color = input("enter color: ")
#charge > 35
#numChars > 5 add $4
#pine add 0,  oak add $20 
#black white 0,  gold add $15
if numChars > 5:
    charge += (numChars-5) * 4.00

if color == "gold":
    charge += 15.00

if woodType == "oak":
    charge += 20.00


print("The charge for this sign is $" + str(charge))