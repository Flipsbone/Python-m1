class GardenManager:
    """
    This is a class attribute to track how many managers exist
    """
    total_garden = 0

    def __init__(self) -> None:
        self.garden = {}
        GardenManager.total_garden += 1

    def add_plant(self, owner_name: str, plant_objet):
        if owner_name is not self.garden:
            self.garden[owner_name] = []
        self.garden[owner_name].append(plant_objet)
        print(f"Added {plant_objet.name} to {owner_name}'s garden")


class Plant:
    """
    Blueprint for a plant that can grow and age.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
    """
    def __init__(self, name: str, height: int) -> None:
        self.name = name.capitalize()
        self.__height = 0
        self.set_height(height)

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

    def grow_plant(self, height) -> int:
        self.__height += 1


class FloweringPlant(Plant):
    """
    Specialized plant type that can bloom and has a color.
    Attributes:
        color (str): The color of the plant.
        Inherited attributes (name,height) are managed by the Plant class.
    """
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    A competitive-grade FloweringPlant with scoring metrics.
    Attributes:
        prize_points (int): Numerical value representing the flower's quality..
        Inherited attributes (name,height,color) are managed
        by the Plant/flowering class.
    """
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_point = prize_points


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    oak = Plant("Oak Tree", 100)
    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    print(f"\nTotal gardens managed: {GardenManager.total_gardens}")
    alice_plants = manager.gardens.get("Alice", [])
    print(f"Number of plants in Alice's garden: {len(alice_plants)}")