import json
from vehical import Vehicle
class car(Vehicle):
    def __init__(self,model="",company="",lisence_plate="",rent_price=0,avaiable="yes",car_name="",car_type=""):
        super().__init__(model,company,lisence_plate,rent_price,avaiable)
        self.car_name=car_name
        self.car_type=car_type

    def add_vehicle(self):

        car_info={"Car Name":self.car_name,
                  "Car Type":self.car_type,
                  "Availability":self.available,
                   "Model":self.model,
                    "Company":self.company,
                     "plate no":self.lisence_plate,
                     "Rent per day":self.rent_price}
        car_data=[]
        with open("/Users/apple/Documents/Vehical-rental-system/cars.json", 'a+') as fileobj:
            fileobj.seek(0)
            try:

              car_data=json.load(fileobj)

            except json.JSONDecodeError:
                car_data=[]

            car_data.append(car_info)

        with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'w') as fileobj:
            json.dump(car_data,fileobj,indent=4)
        print("Car successfully added")

    def show_all_vehicels(self):

        with open("/Users/apple/Documents/Vehical-rental-system/cars.json","r") as fileobj:
            try:

              CARS=json.load(fileobj)
              print("ALL CARS AVAILABLE IN GERAGE ARE LISTED BELOW:\n")
              for carz in CARS:
                 print(carz['Car Name'].upper() + "'s INFO")
                 print(f"Car Name: {carz["Car Name"].upper()}")
                 print(f"Car type: {carz['Car Type']}")
                 print(f"Availability: {carz['Availability']}")
                 print(f"Model: {carz["Model"]}")
                 print(f"Company: {carz["Company"]}")
                 print(f"Plate No: {carz['plate no']}")
                 print(f"Rent per day {carz['Rent per day']}\n")
              print("_____________________________________")

            except  json.JSONDecodeError:
                print("FILE contain nothing")

    def search_vehicel(self):
        with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'r') as fileobj:
          name=input("Enter the car name you want to search from collection")
          try:


              CARS=json.load(fileobj)
              for carz in CARS:
                 if name.lower()==carz["Car Name"].lower():

                   print(f"Car Name: {carz["Car Name"]}")
                   print(f"Car Type: {carz['Car Type']}")
                   print(f"Availability: {carz['Availability']}")
                   print(f"Model: {carz["Model"]}")
                   print(f"Company: {carz["Company"]}")
                   print(f"Plate No: {carz['plate no']}")
                   print(f"Rent per day {carz['Rent per day']}\n")


          except json.JSONDecodeError:

              print("CAR NOT AVAILABLE")




    def check_availability(self,name,plate):

        with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'r') as fileobj:

            try:
                CARS=json.load(fileobj)
                for carz in CARS:
                    if carz['Car Name'].lower()==name.lower() and carz["plate no"].lower()==plate.lower():
                        if carz["Availability"].lower()=='yes':
                            return True
                return False

            except json.JSONDecodeError:
                print("Car not available")
    def update_the_availability(self,rented,name,plate_no):
        try:
            with open("/Users/apple/Documents/Vehical-rental-system/cars.json","r") as fileobj:
                fileobj.seek(0)
                CARS=json.load(fileobj)
            for carz in CARS:
                 if carz["Car Name"].lower()==name.lower() and carz["plate no"].lower()==plate_no.lower():
                     carz['Availability']='no' if rented else 'yes'
            with open("/Users/apple/Documents/Vehical-rental-system/cars.json","w") as fileobj:
                json.dump(CARS,fileobj,indent=4)
        except json.JSONDecodeError:
            print("JSON FILE ERROR!\n")




