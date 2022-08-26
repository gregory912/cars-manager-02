from car.model.model import Car
from collections import namedtuple


def car_named_tuple(items: Car) -> namedtuple:
    """
    The function converts the Car object to namedtuple
    """
    car = namedtuple("Car", "model price mileage engine car_body wheel file_name")
    return car(items.model, items.price, items.mileage, items.engine, items.car_body, items.wheel, items.file_name)
