#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, h):
        if h < 0:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__h = h

    def get_height(self):
        return self.__h

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 10, 5)
    print("Plant created:", rose.name)
    print(f"Height updated: {rose.get_height()}cm [ok]")
