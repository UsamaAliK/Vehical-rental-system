import json
from vehical import Vehicle
class car(Vehicle):
    def __init__(self,model,company,lisence_plate,rent_price,car_name):
        super().__init__(model,company,lisence_plate,rent_price)
        self.car_name=car_name

    def add_vehicle(self):

        car_info={"Car Name":self.car_name,
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









#cars=car("sadasd","sadasfasf",5346346,"543g","gthrt34")
cars2=car("2024","TOYOTA","AKA 306","200000 per day","LAND CRUSER")
#cars2.add_vehicle()
#cars.add_vehicle()
cars2.show_all_vehicels()