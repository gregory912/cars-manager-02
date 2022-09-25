from car.model.model import Car
from car.model.model_enums import *
from .sorting import *
from .statistics import CarStatistics
from .enums import *
from decimal import Decimal


class CarsService:
    def __init__(self, cars: list[Car]):
        self.cars_obj = cars

    def __str__(self):
        """
        Enter all car data into the appropriate format for display
        """
        cars = ""
        for item in self.cars_obj:
            cars += f"""
                    Car model: {item.model}
                    Price: {item.price}
                    Mileage: {item.mileage}
                    Engine: {item.engine.type.name} {item.engine.power}
                    Car Body: {item.car_body.color.name} {item.car_body.type.name} 
                    Components: {', '.join(item.car_body.components)}
                    Wheel: {item.wheel.model} {item.wheel.size} {item.wheel.type.name}
                    """
        return cars

    def sort_cars(self, sort_type: Enum, descending: bool = False) -> list[Car]:
        """
        The method returns a collection of cars sorted according to the criterion given as an argument.
        The method should be able to sort according to the number of components, engine power and tire size.
        Additionally, the method should enable sorting in ascending and descending order.
        """
        if sort_type == SortType.COMPONENTS:
            return SortingComponents().sort_cars(self.cars_obj, descending)
        elif sort_type == SortType.ENGINE_POWER:
            return SortingEnginePower().sort_cars(self.cars_obj, descending)
        elif sort_type == SortType.WHEEL_SIZE:
            return SortingWheelSize().sort_cars(self.cars_obj, descending)

    def get_car_body_with_entered_price(self, car_body: Enum, min_price: Decimal, max_price: Decimal) -> list[Car]:
        """
        The method returns a collection of cars with a specific type of body passed
        as the argument (CarBodyType) and a price in the range <a, b>,
        where a and b are the next arguments of the method.
        """
        if min_price < 0 or min_price > max_price:
            raise ValueError('The entered range is not correct')
        return [obj for obj in self.cars_obj if obj.has_price_between(min_price, max_price) and obj.has_type(car_body)]

    def get_sorted_cars_with_entered_engine_type(self, engine_type: Enum) -> list[Car]:
        """
        The method returns an alphabetically sorted collection of car models
        that have the EngineType passed as the argument to the method.
        """
        cars = [item for item in self.cars_obj if item.has_engine_type(engine_type)]
        return sorted(cars, key=lambda item: item.model)

    def get_statistics_of_cars(self, attribute: Enum) -> tuple[int, float, int]:
        """
        The method returns statistical data for the size given as an argument.
        Acceptable sizes are price, mileage and engine power.
        The statistics should include the smallest value,
        the highest value and the mean value.
        """
        if attribute == Statistic.PRICE:
            return CarStatistics([x.price for x in self.cars_obj]).get_min_avg_max
        elif attribute == Statistic.MILEAGE:
            return CarStatistics([x.mileage for x in self.cars_obj]).get_min_avg_max
        elif attribute == Statistic.POWER:
            return CarStatistics([x.engine.power for x in self.cars_obj]).get_min_avg_max

    def get_mileage_sorted_descending(self) -> dict[Car, int]:
        """
        The method returns a dict in which the key is an object of class Car,
        while the value is the number of kilometers that the car has traveled.
        The pairs on the dict are sorted in descending order by value.
        """
        ziped_values = zip(self.cars_obj, [x.mileage for x in self.cars_obj])
        return dict(sorted(ziped_values, key=lambda x: x[1], reverse=True))

    def get_list_of_cars_with_given_tire(self) -> dict[TyreType, list]:
        """
        The method returns a dict where the key is the type of tire (TyreType) and
        the value is a list of cars with this type of tire. The dict is sorted in descending
        order by the number of items in the collection.
        """
        winter_tires, summer_tires = [], []
        for car in self.cars_obj:
            winter_tires.append(car) if car.is_winter() else summer_tires.append(car)
        dict_ = {TyreType.WINTER: winter_tires, TyreType.SUMMER: summer_tires}

        return dict(sorted(dict_.items(), key=lambda y: len(y[1]), reverse=True))

    def return_cars_that_have_entered_components(self, components: list[str]) -> list[Car]:
        """
        The method returns a collection of cars that have all
        the components from the collection passed as an argument.
        The collection is sorted alphabetically by car model name.
        """
        return [item for item in self.cars_obj if item.has_components(components)]
