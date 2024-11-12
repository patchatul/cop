AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

menu = """********************************
AutoCountry Vehicle Finder v0.4
********************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
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
    elif choose_menu == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ") 
        AllowedVehiclesList.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle')
#unit test 1  
    elif choose_menu == "4": 
        remove_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        sure_to_remove = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no) ')
#unit test 2 3 
        if sure_to_remove.lower() == "yes" and remove_vehicle in AllowedVehiclesList:
            AllowedVehiclesList.remove(remove_vehicle)
            print(f'You have REMOVED "{remove_vehicle}" as an authorized vehicle')
    elif choose_menu == "5":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
