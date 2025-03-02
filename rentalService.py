#create a class called Vehicles
class vehicles:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def get_rental_price_per_day(self):
            return self._rental_price_per_day
        
    def set_rental_price_per_day(self, price):
        if price < 0:
            raise ValueError("Rental price per day cannot be negative.")
        self._rental_price_per_day = price

    def display_info(self):
        
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nRental Price Per Day: {self.rental_price_per_day}"
        
    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days
    
#create a class called Car that inherits from Vehicles
class Car(vehicles):
    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        return super().display_info() + f"\nSeating Capacity: {self.seating_capacity}"
    
#created a class called Motorbike that inherits from Vehicles
class motorbike(vehicles):
    def __init__(self, brand, model, year, rental_price_per_day,engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f"\nEngine Capacity: {self.engine_capacity}"
    
#a function to show polymorphism
def show_vehicle_info(vehicle):
    vehicle.display_info()
    
