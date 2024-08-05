from Car import car
from BIKES import Bike
from customer import Customer
from ADMIN import Admin
import os
import time

who = int(input("PRESS 1 IF YOU ARE CUSTOMER OR PRESS 2 IF YOU ARE ADMIN: "))

while who == 1 or who == 2:
    if who == 1:
        customer = Customer()
        op = -1



        while op != 0:
            os.system('clear')
            print("-------WELCOME TO VEHICLE RENTING GARAGE--------\n")
            print("PRESS 1 IF YOU WANT TO SEE ALL THE CARS AND BIKES.")
            print("PRESS 2 IF YOU WANT TO SEARCH A CAR OR BIKE.")
            print("PRESS 3 IF YOU WANT TO RENT A VEHICLE.")
            print("PRESS 4 IF YOU WANT TO RETURN A VEHICLE.")
            print("PRESS 0 IF YOU WANT TO EXIT.")
            op = int(input())
            if op == 1:
                os.system("clear")
                choice = input("PRESS 1 FOR BIKES AND 2 FOR CARS: ")
                if choice == '1':
                    customer.show_vehcicals(Bike())
                elif choice == '2':
                    customer.show_vehcicals(car())
            elif op == 2:
                os.system("clear")
                choice = input("PRESS 1 IF YOU WANT TO SEARCH  FOR BIKES AND 2 IF FOR CARS: ")
                if choice == '1':
                    customer.search_vehical(Bike())
                elif choice == '2':
                    customer.search_vehical(car())
            elif op == 3:
                os.system("clear")
                choice = input("PRESS 1 FOR RENTING A BIKE AND 2 FOR RENTING A CAR: ")
                if choice == '1':
                    customer.rent_a_bike()
                elif choice == '2':
                    customer.Rent_a_car()
            elif op == 4:
                os.system("clear")
                choice = input("PRESS 1 FOR RETURNING A BIKE AND 2 FOR RETURNING A CAR: ")
                if choice == '1':
                    customer.return_bike()
                elif choice == '2':
                    customer.return_car()
            elif op == 0:
                break

    elif who == 2:
        admin = Admin()
        op = -1
        os.system('clear')
        while op != 0:
            os.system('clear')
            print("-------WELCOME TO VEHICLE RENTING GARAGE ADMIN PANEL--------\n")
            print("PRESS 1 TO ADD A NEW VEHICLE.")
            print("PRESS 2 TO SHOW ALL VEHICLES.")
            print("PRESS 3 TO SEARCH A VEHICLE.")
            print("PRESS 4 TO SHOW RENTED CARS RECORD.")
            print("PRESS 5 TO SHOW RENTED BIKES RECORD.")
            print("PRESS 6 TO SHOW ALL RECORDS.")
            print("PRESS 0 TO EXIT.")
            op = int(input())
            if op == 1:
                os.system("clear")
                choice = input("PRESS 1 TO ADD A BIKE AND 2 TO ADD A CAR: ")
                if choice == '1':
                    admin.add_bike()
                elif choice == '2':
                    admin.add_car()
            elif op == 2:
                os.system("clear")
                admin.show_vehcical()
            elif op == 3:
                os.system("clear")
                admin.search_vehical()
            elif op == 4:
                os.system("clear")
                admin.show_cars_records()
            elif op == 5:
                os.system("clear")
                admin.show_bike_records()
            elif op == 6:
                os.system("clear")
                admin.show_all_record()
            elif op == 0:
                break

    who = int(input("PRESS 1 IF YOU ARE CUSTOMER OR PRESS 2 IF YOU ARE ADMIN: "))
