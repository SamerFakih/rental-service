#create a class called Vehicles
class vehicles:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def display_info(self):
        
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nRental Price Per Day: {self.rental_price_per_day}"
    
my_vehicle = vehicles("Toyota", "Corolla", 2015, 100)

print(my_vehicle.display_info())

