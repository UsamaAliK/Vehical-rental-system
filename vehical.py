from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,model,company,lisence_plate,rent_price,available):
        self.model=model
        self.company=company
        self.lisence_plate=lisence_plate
        self.rent_price=rent_price
        self.available=available
    @abstractmethod
    def add_vehicle(self):
        raise NotImplementedError
    @abstractmethod
    def show_all_vehicels(self):
        raise NotImplementedError

    @abstractmethod
    def search_vehicel(self):
        raise NotImplementedError

    @abstractmethod
    def check_availability(self,name,plate):
        raise NotImplementedError


    @abstractmethod
    def rent_car(self):
        raise NotImplementedError







