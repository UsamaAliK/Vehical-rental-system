import json
from vehical import Vehicle
class car(Vehicle):
    def __init__(self,model,company,lisence_plate,rent_price,car_name,car_type):
        super().__init__(model,company,lisence_plate,rent_price)
        self.car_name=car_name
        self.car_type=car_type

    def add_vehicle(self):

        car_info={"Car Name":self.car_name,
                  "Car "
                   "Model":self.model,
                    "Company":self.company,
                     "plate no":self.lisence_plate,
                     "Rent per day":self.rent_price}
        car_data=[]
        with open("/Users/apple/Documents/Vehical-rental-system/cars.json", 'r') as fileobj:
            car_data=json.load(fileobj)

        car_data.append(car_info)

        with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'w') as fileobj:
            json.dump(car_data,fileobj,indent=4)
        print("Car successfully added")

    def show_all_vehicels(self):

        with open("/Users/apple/Documents/Vehical-rental-system/cars.json","r") as fileobj:
            CARS=json.load(fileobj)
            for carz in CARS:

                print(f"Car Name: {carz["Car Name"]}")
                print(f"Model: {carz["Model"]}")
                print(f"Company: {carz["Company"]}")
                print(f"Plate No: {carz['plate no']}")
                print(f"Rent per day {carz['Rent per day']}\n")

    def search_vehicel(self):
        with open("/Users/apple/Documents/Vehical-rental-system/cars.json",'r') as fileobj:
            name=input("Enter the car name you want to search from collection")
            CARS=json.load(fileobj)
            for carz in CARS:
                if name==carz["Car Name"]:

                  print(f"Car Name: {carz["Car Name"]}")
                  print(f"Model: {carz["Model"]}")
                  print(f"Company: {carz["Company"]}")
                  print(f"Plate No: {carz['plate no']}")
                  print(f"Rent per day {carz['Rent per day']}\n")





    





