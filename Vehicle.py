class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "240 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"


# Function to display car details using polymorphism
def car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")


# Create instances of both classes
bmw_car = BMW()
ferrari_car = Ferrari()

# Display details for BMW
print("BMW Details:")
car_details(bmw_car)

print("\nFerrari Details:")
# Display details for Ferrari
car_details(ferrari_car)
