#!/usr/bin/env python3

class GardenManager:
    """
    This is a class to manage multiple gardens and their plants.
    Attributes:
        total_gardens (int): Class variable to track total gardens created.
        garden (dict): Instance variable to hold gardens and their plants.
    """
    total_gardens = 0

    class GardenStats:
        """ Nested class to hold garden statistics. """
        @staticmethod
        def get_type_counts(plants: list) -> dict:
            """ Return counts of each plant type in the garden. """
            type_counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for the_plant in plants:
                if isinstance(the_plant, PrizeFlower):
                    type_counts["PrizeFlower"] += 1
                elif isinstance(the_plant, FloweringPlant):
                    type_counts["FloweringPlant"] += 1
                elif isinstance(the_plant, Plant):
                    type_counts["Plant"] += 1
            return type_counts

        @staticmethod
        def calculate_score(plants: list) -> int:
            """ Calculate total prize points for PrizeFlowers in the garden."""
            score = sum(p.get_height() for p in plants)
            for the_plant in plants:
                if hasattr(the_plant, 'prize_point'):
                    score += (the_plant.prize_point * 4)
            return score

    @classmethod
    def create_garden(cls):
        """ Create a new garden and increment the total gardens count. """
        cls.total_gardens += 1
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        """ Validate that height is non-negative. """
        return height >= 0

    def __init__(self) -> None:
        self.garden = {}

    def add_plant(self, owner_name: str, plant_objet) -> None:
        """ Add a plant object to the specified owner's garden."""
        if owner_name not in self.garden:
            self.garden[owner_name] = []
        self.garden[owner_name].append(plant_objet)
        print(f"Added {plant_objet.name} to {owner_name}'s garden")

    def growth_all_plants(self, owner_name: str) -> None:
        """ Grow all plants in the specified owner's garden."""
        if owner_name in self.garden:
            print(f"\n{owner_name} is helping all plants grow...")
            for plants in self.garden[owner_name]:
                plants.grow_plant()
                print(f"{plants.name} grew {plants.get_growth_amount()}cm")

    def display_garden(self, owner_name: str) -> None:
        """ Display all plants in the specified owner's garden."""
        if owner_name in self.garden:
            print(f"\n=== {owner_name}'s Garden Report ===\nPlants in garden:")
            for plants in self.garden[owner_name]:
                info = f"- {plants.name}: {plants.get_height()}cm"
                if isinstance(plants, FloweringPlant):
                    info += f", Color: {plants.color} flowers (blooming)"
                if isinstance(plants, PrizeFlower):
                    info += f", Prize Points: {plants.prize_point}"
                print(info)


class Plant:
    """
    Blueprint for a plant that can grow and age.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        growth_amount (int): The amount the plant grows each time.
    """
    def __init__(self, name: str, height: int, growth_amount: int) -> None:
        self.name = name.capitalize()
        self.__height = 0
        self.set_height(height)
        self.__growth_amount = 0
        self.set_growth_amount(growth_amount)

    def set_height(self, height: int) -> None:
        """Validate and set height if non-negative."""
        if height < 0:
            print(
                "Invalid operation attempted: "
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height

    def get_height(self) -> int:
        """Return the protected height."""
        return self.__height

    def set_growth_amount(self, growth_amount: int) -> None:
        """Validate and set growth amount if non-negative."""
        if growth_amount < 0:
            print(
                "Invalid operation attempted: "
                f"growth amount {growth_amount}cm [REJECTED]")
            print("Security: Negative growth amount rejected\n")
        else:
            self.__growth_amount = growth_amount

    def get_growth_amount(self) -> int:
        """Return the protected growth amount."""
        return self.__growth_amount

    def grow_plant(self) -> None:
        """Increase the plant's height by its growth amount."""
        self.__height += self.__growth_amount


class FloweringPlant(Plant):
    """
    Specialized plant type that can bloom and has a color.
    Attributes:
        color (str): The color of the plant.
        Inherited attributes (name,height,growth_amount)
        are managed by the Plant class.
    """
    def __init__(self, name: str, height: int, growth_amount: int, color: str):
        super().__init__(name, height, growth_amount)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    A competitive-grade FloweringPlant with scoring metrics.
    Attributes:
        prize_points (int): Numerical value representing the flower's quality.
        Inherited attributes (name,height,growth_amount,color) are managed
        by the Plant/flowering class.
    """
    def __init__(
            self, name: str, height: int, growth_amount: int,
            color: str, prize_points: int
            ):
        super().__init__(name, height, growth_amount, color)
        self.prize_point = prize_points


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager()
    oak = Plant("Oak Tree", 100, 1)
    rose = FloweringPlant("Rose", 25, 1, "red")
    sunflower = PrizeFlower("Sunflower", 50, 1, "yellow", 10)

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)
    manager.growth_all_plants("Alice")
    manager.display_garden("Alice")

    bob_cactus = Plant("Cactus", 10, 2)
    manager.add_plant("Bob", bob_cactus)
    manager.display_garden("Bob")

    print("\nHeight validation test:"
          f"{GardenManager.validate_height(sunflower.get_height())}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
