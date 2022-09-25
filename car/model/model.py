from .model_components import *
from decimal import Decimal


class Car:
    def __init__(self, json_data: dict, file_name: str):
        self.model = json_data["model"]
        self.price = Decimal(json_data["price"])
        self.mileage = json_data["mileage"]
        self.engine = Engine.get_model(json_data["engine"])
        self.car_body = CarBody.get_model(json_data["carBody"])
        self.wheel = Wheel.get_model(json_data["wheel"])
        self.file_name = file_name
        self._validate_elements()

    def _validate_elements(self):
        """
        Check that the elements entered into the class are in the correct format
        """
        if not validate_model(self.model):
            raise ValueError("The entered model is invalid.")
        if not validate_greater_than_0(self.price):
            raise ValueError("The entered price is incorrect.")
        if not validate_greater_than_0(self.mileage):
            raise ValueError("The entered mileage is incorrect.")

    def has_price_between(self, min_price: Decimal, max_price: Decimal) -> bool:
        """
        Check if the price of a given car is within the entered range
        """
        return min_price <= self.price <= max_price

    def has_type(self, expected_type: Enum) -> bool:
        """
        Check if the expected type is the same as the type of the object
        """
        return expected_type == self.car_body.type

    def has_engine_type(self, expected_type: Enum) -> bool:
        """
        Check if the expected type is the same as the engine type of the object
        """
        return expected_type == self.engine.type

    def is_winter(self) -> bool:
        """
        Check if the car has a winter tire
        """
        return TyreType.WINTER == self.wheel.type

    def has_components(self, components: list):
        """
        Check that the entered components are contained in the components of the object
        """
        return set(components).issubset(set(self.car_body.components))
