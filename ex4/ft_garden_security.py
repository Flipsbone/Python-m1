#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        print("Plant created:", name.capitalize())
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, h):
        if h < 0:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__h = h
            print(f"Height updated: {h}cm [ok]")

    def get_height(self):
        return self.__h

    def set_age(self, age):
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
    r = Plant("rose", 25, 30)
    r.set_height(-10)
    print(f"Current plant: {r.name} ({r.get_height()}cm, {r.get_age()} days)")
