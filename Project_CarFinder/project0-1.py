
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

menu = """********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. Exit
"""
#unit test1
print(menu)
choose_menu = int(input("Enter Here:"))

#unit test2
if choose_menu == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for i in AllowedVehiclesList:
        print(i)
#unit test3
elif choose_menu == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

# multiple lines use """