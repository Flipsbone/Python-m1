#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    garden_center = [rose, oak, cactus, sunflower, fern]

    count = 0
    for item in garden_center:
        count += 1

    print("=== Plant Factory Output ===")
    for i in range(count):
        plt = garden_center[i]
        print(f"Created: {plt.name} ({plt.height}cm, {plt.age} days)")
    print("\nTotal plants created:", count)
