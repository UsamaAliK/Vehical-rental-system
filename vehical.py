from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,model="",company="",lisence_plate="",rent_price=0,available=""):
        self.model=model
        self.company=company
        self.lisence_plate=lisence_plate
        self.rent_price=rent_price
        self.available=available

    def add_vehicle(self):
        raise NotImplementedError
    def show_all_vehicels(self):
        raise NotImplementedError


    def search_vehicel(self):
        raise NotImplementedError


    def check_availability(self,name,plate):
        raise NotImplementedError


    def update_the_availability(self,rented,name,plate_no):
        raise NotImplementedError











