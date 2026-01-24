#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int):
        self.name = name.capitalize()
        self.__height = 0
        self.set_height(height)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(
                "Invalid operation attempted: "
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height

    def get_height(self) -> int:
        return self.__height


class FloweringPlant (Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower (FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_point: int):
        super().__init__(name, height, color)
        self.prize_point = prize_point


class GardenManager:
    nb_gardens = 0

    def __init__(self, name: str):
        self.gardens = {}
        self.name = name

    def add_plant(self, garden_name: str, plants: Plant):
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
        self.gardens[garden_name].append(plants)
        print(f"Added {plants.name} to {garden_name}'s garden")

    def display_garden(self, garden_name: str):
        if garden_name not in self.gardens:
            print("Garden name not found")
        else:
            print(f"\n=== {garden_name}'s Garden Report ===")
            print(f"Plants in {self.name}")
            for plant in self.gardens[garden_name]:
                info = f"- {plant.name}: {plant.get_height()}cm"
                if isinstance(plant, FloweringPlant):
                    info += f", Color: {plant.color} flowers (blooming)"
                if isinstance(plant, PrizeFlower):
                    info += f", Prize Points: {plant.prize_point}"
                print(info)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    garden = GardenManager("garden")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    garden.add_plant("Alice", oak)
    garden.add_plant("Alice", rose)
    garden.add_plant("Alice", sunflower)
    garden.display_garden("Alice")
