#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        if height < 0:
            raise ValueError(
                    "Invalid operation attempted: "
                    f"height {height}cm [REJECTED]")
        else:
            self.__height = height

    def set_age(self, age: int):
        if age < 0:
            raise ValueError(
                    f"Invalid operation attempted: age {age}"
                    "days [REJECTED]")
        else:
            self.__age = age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter: int):
        if trunk_diameter < 0:
            raise ValueError(
                        "Invalid operation attempted: "
                        f"diameter {trunk_diameter}cm [REJECTED]")
        else:
            self.__trunk_diameter = trunk_diameter

    def get_trunk_diameter(self):
        return self.__trunk_diameter

    def produce_shade(self, trunck_diameter: int):
        d_trunk_m = trunck_diameter / 100
        d_crown_m = d_trunk_m * 20
        radius_m = d_crown_m / 2
        shade = 3.14 * (radius_m ** 2)
        print(f"{self.name} provides {shade:.0f} square meters of shade\n")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: int,
        age: int, harvest_season: str, nutritional_value: str
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value.capitalize()


if __name__ == "__main__":
    print("===  Garden Plant Types ===\n")
    rose = Flower("rose", 25, 30, "red")
    print(
        f"{rose.name} (Flower): {rose.get_height()}cm, {rose.get_age()} days, "
        f"{rose.color} color")
    rose.bloom()
    oak = Tree("oak", 500, 1825, 50)
    print(
        f"{oak.name} (Tree): {oak.get_height()}cm, {oak.get_age()} days, "
        f"{oak.get_trunk_diameter()} diameter")
    oak.produce_shade(oak.get_trunk_diameter())
    tomato = Vegetable("tomato", 80, 90, "summer", "c")
    print(
        f"{tomato.name} (Vegetable): {tomato.get_height()}cm, "
        f"{tomato.get_age()} days, {tomato.harvest_season} harvest\n"
        f"{tomato.name} is rich in vitamin {tomato.nutritional_value}")
