from typing import List
from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):

        self.phone_number: str = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value.startswith("0") and len(value) == 10 and value.isdigit()):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
