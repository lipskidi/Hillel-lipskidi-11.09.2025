import random

class Car:
    def __init__(self, model: str, color: str):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance: int):
        if distance > self.fuel:
            distance = self.fuel

        self.trip_distance += distance
        self.fuel -= distance


def race_simulation(desired_dist: int):
    car1 = Car("Toyota", "Red")
    car2 = Car("Honda", "Blue")
    car3 = Car("Nissan", "Yellow")

    cars = [car1, car2, car3]

    winner = None

    while True:
        for car in cars:
            step = random.randrange(0, 9)
            car.move(step)
            if car.trip_distance >= desired_dist:
                winner = car
                break

        if winner is not None:
            break

    print(f"Переміг автомобіль {winner.model} з дистанцією {winner.trip_distance}")

    for car in cars:
        print(f"{car.model} ({car.color}): проїхав {car.trip_distance}, залишилось палива {car.fuel}")

if __name__ == "__main__":
    race_simulation(2)
