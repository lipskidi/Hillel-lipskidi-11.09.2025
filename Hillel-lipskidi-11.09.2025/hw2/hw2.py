import random
from typing import List, Optional

class Car:
    def __init__(self, model: str, color: str):
        self.fuel: int = random.randrange(0, 9)
        self.trip_distance: int = 0
        self.model: str = model
        self.color: str = color

    def move(self, distance: int) -> int:

        if distance <= 0 or self.fuel <= 0:
            return 0
        actual = min(distance, self.fuel)
        self.trip_distance += actual
        self.fuel -= actual
        return actual

def race_simulation(desired_dist: int, seed: Optional[int] = None) -> None:
    if seed is not None:
        random.seed(seed)

    cars: List[Car] = [
        Car("Toyota", "Red"),
        Car("Honda", "Blue"),
        Car("Nissan", "Black"),
    ]

    winner: Optional[Car] = None
    max_rounds = 10000
    round_count = 0

    while True:
        round_count += 1
        if round_count > max_rounds:
            print("Досягнуто максимуму ітерацій — зупиняю гонку як страховку.")
            break

        moved_any = False

        for car in cars:
            step = random.randrange(0, 9)  # 0..8
            moved = car.move(step)
            if moved > 0:
                moved_any = True

            if car.trip_distance >= desired_dist:
                winner = car
                break

        if winner is not None:
            print(f"Переміг автомобіль {winner.model} — пройшов {winner.trip_distance} одиниць.")
            break

        if not moved_any:
            print("Жоден автомобіль не може більше рухатися (немає палива або ходи 0). Гонка зупинена.")
            break

    print("\nПідсумки гонки:")
    for car in cars:
        print(f"{car.model} ({car.color}) — пройшов: {car.trip_distance}, паливо: {car.fuel}")

if __name__ == "__main__":
    race_simulation(desired_dist=50, seed=42)
