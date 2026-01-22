#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        print("Plant created:", name.capitalize())
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        if height < 0:
            print(
                "Invalid operation attempted: "
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [ok]")

    def get_height(self):
        return self.__height

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {age} days [ok]\n")

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    flower = Plant("rose", 25, 30)
    flower.set_height(-10)
    print(
        f"Current plant: {flower.name}"
        f"({flower.get_height()}cm, {flower.get_age()} days)")
