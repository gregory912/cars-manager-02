from .model_components import *


class Car:
    def __init__(self, json_data: dict, file_name: str):
        self.model = json_data["model"]
        self.price = json_data["price"]
        self.mileage = json_data["mileage"]
        self.engine = Engine(**json_data["engine"])
        self.car_body = CarBody(**json_data["carBody"])
        self.wheel = Wheel(**json_data["wheel"])
        self.file_name = file_name
        self._validate_elements()

    def _validate_elements(self):
        """
        Check that the elements entered into the class are in the correct format
        """
        if not validate_model(self.model):
            raise ValueError("The entered model is invalid.")
        if not validate_price_mileage(self.price):
            raise ValueError("The entered price is incorrect.")
        if not validate_price_mileage(self.mileage):
            raise ValueError("The entered mileage is incorrect.")
