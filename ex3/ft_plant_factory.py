#!/usr/bin/env python3
"""This module defines a Plant class and demonstrates creating multiple plant
instances using a list comprehension."""


class Plant:
    """
    Blueprint representing a plant in the garden.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        age (int): The age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    garden_center = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    total_len = len(garden_center)
    myplant = [Plant(name, height, age) for name, height, age in garden_center]
    print("=== Plant Factory Output ===")
    for k in range(total_len):
        plt = myplant[k]
        print(f"Created: {plt.name} ({plt.height}cm, {plt.age} days)")
    print("\nTotal plants created:", total_len)
