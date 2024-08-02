import json

from vehical import Vehicle
class Bike(Vehicle):
    def __init__(self,bike_name="",model="",company="",lisence_plate="",rent_price=0,available=""):
        super().__init__(model,company,lisence_plate,rent_price,available)
        self.bike_name=bike_name



    def add_vehicle(self):
        bike_info={"BIKE NAME":self.bike_name,
                   "MODEL":self.model,
                   "COMPANY":self.company,
                   "PLATE NO":self.lisence_plate,
                   "RENT PER DAY":self.rent_price,
                   "AVAILABILITY":self.available}
        bike_data=[]
        with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json","a+") as fileobj:
            fileobj.seek(0)
            try:
                bike_data=json.load(fileobj)

            except json.JSONDecodeError:
                bike_data=[]
            bike_data.append(bike_info)

        with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json",'w') as fileobj:
            json.dump(bike_data,fileobj,indent=4)


        print("BIKE ADDED SUCCESSFULLY")



    def search_vehicel(self):
        name=input("ENTER THE NAME OF BIKE YOU WANT TO SEARCH: ")
        with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json","r") as fileobj:
            try:
                BIKES=json.load(fileobj)
                for bikez in BIKES:
                   if name==bikez["BIKE NAME"]:
                        print(f"BIKE NAME: {bikez["BIKE NAME"]}")
                        print(f"MODEL: {bikez["MODEL"]}")
                        print(f"COMPANY: {bikez['COMPANY']}")
                        print(f"PLATE NO: {bikez['PLATE NO']}")
                        print(f"RENT PER DAY: {bikez["RENT PER DAY"]}")
                        print(f"AVAILABILITY: {bikez['AVAILABILITY']}")
                   else:
                       print("NO BIKE FOUND WITH THIS NAME\n")
            except json.JSONDecodeError:
                print("BIKE NOT FOUND!\n")


    def show_all_vehicels(self):
        with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json",'r') as fileobj:
            fileobj.seek(0)
            try:
                BIKES=json.load(fileobj)
                for bikez in BIKES:
                   print(f"BIKE NAME: {bikez["BIKE NAME"]}")
                   print(f"MODEL: {bikez["MODEL"]}")
                   print(f"COMPANY: {bikez['COMPANY']}")
                   print(f"PLATE NO: {bikez['PLATE NO']}")
                   print(f"RENT PER DAY: {bikez["RENT PER DAY"]}")
                   print(f"AVAILABILITY: {bikez['AVAILABILITY']}\n")
            except json.JSONDecodeError:
                print("THERE IS NO BIKE IN GERAGE\n ")

    def check_availability(self,name,plate):
        with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json",'r') as fileobj:
            fileobj.seek(0)
            try:
                BIKES=json.load(fileobj)
                for bikez in BIKES:
                    if bikez["BIKE NAME"]==name and bikez['PLATE NO']==plate:
                        if bikez["AVAILABILITY"].lower()=='yes':
                            return True
                return False

            except json.JSONDecodeError:
                print("JSON FILE ERROR")



    def update_the_availability(self,rented,name,plate_no):

           try:
               with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json", 'r') as fileobj:
                   fileobj.seek(0)

                   BIKES=json.load(fileobj)

               for bikez in BIKES:
                    if bikez["BIKE NAME"]==name and bikez["PLATE NO"]==plate_no:
                        bikez["AVAILABILITY"] = 'NO' if rented else 'yes'
               with open("/Users/apple/Documents/Vehical-rental-system/BIKES.json",'w') as fileobj:
                    json.dump(BIKES,fileobj,indent=4)

           except json.JSONDecodeError:
               print("json file error")

















