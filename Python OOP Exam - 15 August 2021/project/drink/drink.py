from abc import ABC


class Drink(ABC):

    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name: str = name
        self.portion: float = portion
        self.price: float = price
        self.brand: str = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if not value > 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty string or white space!")

        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion}ml - {self.price}lv"

