import json
from Car import car
from BIKES import Bike

class Admin:

    def show_cars_records(self):
        try:
          with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json", "r") as fileobj:
             CARS=json.load(fileobj)
             if len(CARS)==0:

                print("CAR RECORDS FILE IS EMPTY!")
                return
        except json.JSONDecodeError:
            print("CAR RECORDS FILE IS EMPTY!")
            return

        with open("/Users/apple/Documents/Vehical-rental-system/rented_cars.json","r") as fileobj:
            fileobj.seek(0)
            try:
                CARS=json.load(fileobj)

                print("RENTED CARS RECORD: \n")
                for carz in CARS:

                    print(f"CUSTOMER NAME: {carz["CUSTOMER NAME"]}")
                    print(f"CINC: {carz["CINC"]}")
                    print(f"CAR NAME: {carz["Car Name"]}")
                    print(f"CAR LISENCE PLATE NO: {carz["Car Plate"]}")
                    print(f"DAYS OF RENT: {carz["DAYS"]}")
                    print(f"RENT PER DAY: {carz["RENT PER DAY"]}")
                    print("-----------------------------------------\n")

            except json.JSONDecodeError:
                print("JSON FILE ERROR IN 'RENTED CARS FILE!'")

    def show_bike_records(self):
        try:

           with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json", "r") as fileobj:
             bikes = json.load(fileobj)
             if len(bikes) == 0:
                print("BIKES RECORDS FILE IS EMPTY")
                return
        except json.JSONDecodeError:
           print("BIKES RECORDS FILE IS EMPTY")
           return


        with open("/Users/apple/Documents/Vehical-rental-system/rented bikes.json", "r") as fileobj:
            fileobj.seek(0)
            try:
                BIKEZ = json.load(fileobj)
                print("RENTED BIKES RECORDS: \n")
                for bike in BIKEZ:
                    print(f"CUSTOMER NAME: {bike["CUSTOMER NAME"]}")
                    print(f"CINC: {bike["CINC"]}")
                    print(f"BIKE NAME: {bike["BIKE NAME"]}")
                    print(f"BIKE LISENCE PLATE NO: {bike["PLATE NO"]}")
                    print(f"DAYS: {bike["DAYS"]}")
                    print(f"RENT PER DAY: {bike["RENT PER DAY"]}")
                    print("---------------------------------------\n")
            except json.JSONDecodeError:
                print("JSON FILE ERROR IN 'rented bikes' FILE")






    def show_all_record(self):
        admin=Admin()
        admin.show_cars_records()
        admin.show_bike_records()


    def add_car(self):
        name=input("ENTER THE NAME OF CAR YOU WANT TO ADD IN COLLECTION: ")
        c_type=input("ENTER THE TYPE OF CAR: SEDAN/SUV: ")
        plate_no=input("ENTER LISENCE PLATE NO OF CAR: ")
        year=input("ENTER THE MODEL OF CAR: ")
        rent=int(input("ENTER CAR'S RENT PER DAY: "))
        company=input("ENTER NAME OF COMPANY: ")
        cars=car(year,company,plate_no,rent,"YES",name,c_type)
        cars.add_vehicle()

    def add_bike(self):
        name=input("ENTER NAME OF BIKE YOU WANT TO ADD IN COLLECTION: ")
        model=input("ENTER MODEL OF THE BIKE: ")
        company=input("ENTER COMPANY NAME THAT MADE THE BIKE: ")
        plate_no=input("ENTER lisence PLATE NO OF BIKE: ")
        rent=int(input("ENTER RENT PER DAY FOR THIS BIKE: "))
        bikes=Bike(name,model,company,plate_no,rent,"yes")
        bikes.add_vehicle()

    def show_vehcical(self):

        cars=car()
        bike=Bike()
        cars.show_all_vehicels()
        bike.show_all_vehicels()


    def search_vehical(self):
        option=input("PRESS 1 IF YOU WANT TO SEARCH A CAR OR PRESS 2 IF YOU WANT TO SEARCH A BIKE: ")

        if option=="1":
            cars=car()
            cars.search_vehicel()
        elif option=="2":
            bike=Bike()
            bike.search_vehicel()


