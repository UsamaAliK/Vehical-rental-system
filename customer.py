import json
from BIKES import Bike
from Car import car
from  vehical import Vehicle
class Customer():


    def Rent_a_car(self):
        print("TAKING CUSTOMER'S INFO \n")
        name=input("ENTER YOUR NAME: ")
        cinc=input("ENTER YOUR CINC: ")
        car_name=input("ENTER THE CAR NAME YOU WANT TO RENT: ")
        plate_no=input("ENTER THE PLATE NUM OF CAR: ")
        days=int(input("ENTER THE NUMBER OF DAYS YOU WANT THE CAR FOR RENT: "))
        rent=0

        cars=car()

        if not cars.check_availability(car_name,plate_no):
            print("SORRY THIS CAR IS NOT AVAILABLE FOR NOW! \n")
            return 0
        else:

            try:
                with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'r') as fileobj:
                    fileobj.seek(0)
                    CARS=json.load(fileobj)

                for carz in CARS:
                     if carz["Car Name"]==car_name and carz["plate no"]==plate_no:
                          rent=int(carz["Rent per day"])

            except json.JSONDecodeError:
                    print("json file error!")


            cus_info={"CUSTOMER NAME":name,
                      "CINC":cinc,
                      "Car Name":car_name,
                      "Car Plate":plate_no,
                      "DAYS":days,
                      "RENT PER DAY":rent}


            with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json",'r') as fileobj:
                fileobj.seek(0)
                try:
                    cus_data=json.load(fileobj)
                except json.JSONDecodeError:
                     cus_data=[]
                cus_data.append(cus_info)

            with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json",'w') as fileobj:
                json.dump(cus_data,fileobj,indent=4)
                cars.update_the_availability(True,car_name,plate_no)


    def rent_a_bike(self):
        cus_name=input("ENTER YOUR NAME PLEASE: ")
        cinc=input("ENTER YOUR CINC NUMBER: ")
        bike_name=input("ENTER THE NAME OF BIKE YOU WANT: ")
        plate_no=input("ENTER IT LISENCE PLATE NO: ")
        days=int(input("ENTER THE NUMBER OF DAYS YOU WANT TO RENT THE CAR: "))
        rent=0
        bike=Bike()

        if not bike.check_availability(bike_name,plate_no):
            print("SORRY THIS BIKE IS NOT AVAILABLE FOR NOW!\n ")
            return

        else:
            with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json",'r') as fileobj:
                try:
                    fileobj.seek(0)
                    BIKES=json.load(fileobj)
                    for bikes in BIKES:
                        if bikes["BIKE NAME"]==bike_name and bikes["PLATE NO"]==plate_no:
                            rent=bikes["RENT PER DAY"]

                except json.JSONDecodeError:
                    print("JSON FILE ERROR!")

            cus_info={"CUSTOMER NAME":cus_name,
                       "CINC":cinc,
                       "BIKE NAME":bike_name,
                        "PLATE NO":plate_no,
                         "DAYS":days,
                          "RENT PER DAY":rent}
            cus_data=[]
            with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json",'r') as fileobj:
                fileobj.seek(0)
                try:

                    cus_data=json.load(fileobj)
                except json.JSONDecodeError:
                    cus_data=[]
                cus_data.append(cus_info)
            with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json",'w') as fileobj:
                json.dump(cus_data,fileobj,indent=4)
                bike.update_the_availability(True,bike_name,plate_no)






    def return_car(self):
        name=input("ENTER YOUR NAME: ")
        car_name=input("ENTER THE CAR NAME THAT YOU ARE RETURNING: ")
        plate_no=input("ENTER LISENCE PLATE NUM OF CAR: ")
        cars = car()
        rent=0
        days=0

        if cars.check_availability(car_name,plate_no):
            print("THIS CAR IS ALREADY RETURNED!\n")
            return


        else:

          with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json",'r') as fileobj:

            try:
              CARS=json.load(fileobj)
              rented_cars=[carz for carz in CARS if not (carz["CUSTOMER NAME"]==name and carz["Car Name"]==car_name and carz["Car Plate"]==plate_no)]
              for car1 in CARS:
                  if car1["CUSTOMER NAME"]==name and car1["Car Name"]==car_name and car1["Car Plate"]==plate_no:
                      rent=car1["RENT PER DAY"]
                      days=car1["days"]



            except json.JSONDecodeError:
              print("json file error")

          with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json",'w') as fileobj:
             fileobj.seek(0)

             json.dump(rented_cars,fileobj,indent=4)

             cars.update_the_availability(False,car_name,plate_no)
          total_coast=rent*days
          print(" HERE IS YOUR BILL!")
          print("NUMBER OF DAYS: "+days)
          print("RENT OF CAR PER DAY IS: "+rent)
          print("TOTAL AMOUNT TO PAY IS: "+total_coast)




    def return_bike(self):
        name=input("ENTER THE YOUR NAME: ")
        bike_name=input("ENTER THE NAME OF BIKE YOU ARE RETURNING: ")
        plate_no=input("ETNER THE LISENCE PLATE NUMBER OF BIKE: ")
        bike=Bike()
        rent=0
        days=0

        if bike.check_availability(bike_name,plate_no):
            print("THIS BIKE IS ALREADY RETURNED! ")
        else:
            with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json",'r') as fileobj:
                try:
                    BIKE=json.load(fileobj)
                    rented_bike=[bikez for bikez in BIKE if not(bikez["CUSTOMER NAME"]==name and bikez["BIKE NAME"]==bike_name and bikez["PLATE NO"]==plate_no)]

                    for bikez in BIKE:
                        if bikez["CUSTOMER NAME"]==name and bikez["BIKE NAME"]==bike_name and bikez["PLATE NO"]==plate_no:
                            days=int(bikez["DAYS"])
                            rent=int(bikez["RENT PER DAY"])
                except json.JSONDecodeError:
                    print("JSON FILE ERROR!\n")
            with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json","w") as fileobj:
                json.dump(rented_bike,fileobj,indent=4)
                bike.update_the_availability(False,bike_name,plate_no)
            total_cost=rent*days
            print("HERE IS YOUR BILL: ")
            print("NUMBER OF DAYS: "+str(days))
            print("RENT PER DAY FOR "+bike_name+" IS "+str(rent))
            print("TOATL AMOUNT YOU HAVE TO PAY IS: "+str(total_cost))


    def show_vehcicals(self,vehicals=Vehicle()):
        vehicals.show_all_vehicels()


    def search_vehical(self,vehicals=Vehicle()):
        vehicals.search_vehicel()