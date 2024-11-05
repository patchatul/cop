AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

menu = """********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
"""

print(menu)
choose_menu = int(input("Enter Here: "))

if choose_menu == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for i in AllowedVehiclesList:
        print(i)
#unit test1
elif choose_menu == 2:
    search_vehicle = input("Please Enter the full Vehicle name: ")
#unit test2
    if search_vehicle in AllowedVehiclesList:
        print(search_vehicle + " is an authorized vehicle")
#unit test3
    else:
        print(search_vehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
elif choose_menu == 3:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")


