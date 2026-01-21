#!/usr/bin/env python 3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.start_height = height

    def update_age(self):
        self.age += 1

    def grow(self, add_cm):
        self.height += add_cm

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    for day in range(1, 8):
        if day == 1 or day == 7:
            print(f"=== Day {day} ===")
            print(rose.get_info())
        rose.grow(1)
        rose.update_age()

    total_height = rose.height - rose.start_height
    print(f"Growth this week: + {total_height}cm")
