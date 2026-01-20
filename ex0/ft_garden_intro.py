#!/usr/bin/env python3

def ft_garden_intro(plant_type: str, height: int, age: int) -> None:
    plant_type = plant_type.capitalize()
    print("Plant:", plant_type)
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_intro("Rose", 25, 30)
    print()
    print("=== End of Program ===")
