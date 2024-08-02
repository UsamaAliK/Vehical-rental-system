import json
from Car import car
class Customer():


    def Rent_a_car(self):
        print("TAKING CUSTOMER'S INFO \n")
        name=input("ENTER YOUR NAME: ")
        cinc=input("ENTER YOUR CINC: ")
        car_name=input("ENTER THE CAR NAME YOU WANT TO RENT: ")
        plate_no=input("ENTER THE PLATE NUM OF CAR ")
        cars=car()

        if not cars.check_availability(car_name,plate_no):
            print("SORRY THIS CAR IS NOT AVAILABLE FOR NOW! \n")
            return 0
        else:

            cus_info={"CUSTOMER NAME":name,
                      "CINC":cinc,
                      "Car Name":car_name,
                      "Car Plate":plate_no}


            with open("/Users/apple/Documents/Vehical-rental-system/customer.json",'r') as fileobj:
                fileobj.seek(0)
                try:
                    cus_data=json.load(fileobj)
                except json.JSONDecodeError:
                     cus_data=[]
                cus_data.append(cus_info)
            with open("/Users/apple/Documents/Vehical-rental-system/customer.json",'w') as fileobj:
                json.dump(cus_data,fileobj,indent=4)
                cars.update_the_availability(True,car_name,plate_no)


















