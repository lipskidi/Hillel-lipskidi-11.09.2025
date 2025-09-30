import random

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.trip_distance = 0
        self.fuel = random.randrange(0, 9)

    def move(self, distance):
        if self.fuel >= distance:
            self.trip_distance += distance
            self.fuel -= distance
        else:
            self.trip_distance += self.fuel
            self.fuel = 0


car1 = Car("BMW", "Black")
car2 = Car("Audi", "Grey")
car3 = Car("Mercedes", "White")

cars = [car1, car2, car3]

desired_dist = 50
winner = None

while True:
    for car in cars:
        step = random.randrange(0, 9)
        car.move(step)

        if car.trip_distance >= desired_dist:
            winner = car
            print(f"Winner: {car.brand}"
                  f"Covered {car.trip_distance}")
            break
    if winner:
        break

print("\n--- Race results ---")
for car in cars:
    print(f"{car.brand} ({car.color}) "f"distance: {car.trip_distance}, "f"fuel: {car.fuel}")
