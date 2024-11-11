AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

menu = """********************************
AutoCountry Vehicle Finder v0.3
********************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. Exit
********************************"""

while True :
    print(menu)
    choose_menu = (input("Enter Here: "))

    if choose_menu == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for i in AllowedVehiclesList:
            print(i)
    elif choose_menu == "2":
        search_vehicle = input("Please Enter the full Vehicle name: ")
        if search_vehicle in AllowedVehiclesList:
            print(search_vehicle + " is an authorized vehicle")
        else:
            print(search_vehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
    #unit test 1
    elif choose_menu == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    #unit test 2-Rivian R1T 3-Ram 1500  
        AllowedVehiclesList.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle')
    elif choose_menu == "4":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
