import json
import os
class Vehicle:
    def __init__(self,model,company,lisence_plate,rent_price):
        self.model=model
        self.company=company
        self.lisence_plate=lisence_plate
        self.rent_price=rent_price
    def add_vehicle(self):
        raise NotImplementedError
    def show_all_vehicels(self):
        raise NotImplementedError

    def search_vehicel(self):
        raise NotImplementedError










