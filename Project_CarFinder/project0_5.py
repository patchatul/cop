   
menu = """********************************
AutoCountry Vehicle Finder v0.5
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
#1. print cars
    if choose_menu == "1":
        with open("Project_CarFinder/cars.txt", mode="r") as db:
            AllowedVehiclesList = db.read()
            db.close()
        print(f'The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: {AllowedVehiclesList}')
#2. search cars
    elif choose_menu == "2":
        search_vehicle = input("Please Enter the full Vehicle name: ")
        if search_vehicle in AllowedVehiclesList:
            print(search_vehicle + " is an authorized vehicle")
        else:
            print(search_vehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
#3. add cars  
    elif choose_menu == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ") 
        with open("Project_CarFinder/cars.txt", mode="a") as db:
            db.write(f'\n{new_vehicle}')
            db.close()
        print(f'You have added "{new_vehicle}" as an authorized vehicle')
#4. remove cars 
    elif choose_menu == "4": 
        remove_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        sure_to_remove = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no) ')
        if sure_to_remove.lower() == "yes":
            with open("Project_CarFinder/cars.txt", mode="r") as db:
                lines = db.readlines()
            with open("Project_CarFinder/cars.txt", mode="w") as db:
                for line in lines:
                    if line.strip() != remove_vehicle:
                        db.write(line)
            print(f'You have REMOVED "{remove_vehicle}" as an authorized vehicle')
#5. exit
    elif choose_menu == "5":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
