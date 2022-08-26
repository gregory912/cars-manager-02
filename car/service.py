from data_loader.json import get_cars
from car.model.model import Car
from car.model.model_enums import TyreType
from car.conversions import car_named_tuple
from statistics import mean
from operator import attrgetter


class CarsService:
    def __init__(self, directory: str):
        self.cars_obj = get_cars(directory)
        self.cars = [car_named_tuple(x) for x in self.cars_obj]

        # print(self.cars)
        # print(self.sort_cars("engine.power", True))
        # print(self.sort_cars("wheel.size", True))
        # print(self.sort_cars("components", True))
        # print(self.sort_cars("components", False))
        # print(self.car_body_with_entered_price("SEDAN", 1000, 2000))
        # print(self.sorted_cars_with_entered_engine_type("DIESEL"))
        # print(self.statistics_of_cars("price"))
        # print(self.statistics_of_cars("mileage"))
        # print(self.statistics_of_cars("power"))
        # print(self.mileage_sorted_descending())
        # print(self.list_of_cars_with_given_tire())
        # print(self.return_cars_that_have_entered_components(["ABS", "AIR CONDITIONING"]))

    def __str__(self):
        """
        Enter all car data into the appropriate format for display
        """
        cars = ""
        for item in self.cars:
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

    def sort_cars(self, sort_type: str, descending: bool = False) -> list[Car]:
        """
        The method returns a collection of cars sorted according to the criterion given as an argument.
        The method should be able to sort according to the number of components, engine power and tire size.
        Additionally, the method should enable sorting in ascending and descending order.
        """
        cars = self.cars.copy()
        if sort_type == 'components':
            tuple_sorted = sorted(cars, key=lambda y: len(y.car_body.components), reverse=descending)
            return tuple_sorted
        else:
            cars.sort(key=attrgetter(sort_type), reverse=descending)
            return cars

    def car_body_with_entered_price(self, car_body: str, min_price: float, max_price: float) -> list[Car]:
        """
        The method returns a collection of cars with a specific type of body passed
        as the argument (CarBodyType) and a price in the range <a, b>,
        where a and b are the next arguments of the method.
        """
        cars = self.cars.copy()
        return list(filter(lambda x: min_price < x.price < max_price and car_body == x.car_body.type.name, cars))

    def sorted_cars_with_entered_engine_type(self, engine_type: str) -> list[Car]:
        """
        The method returns an alphabetically sorted collection of car models
        that have the EngineType passed as the argument to the method.
        """
        cars = self.cars.copy()
        cars = list(filter(lambda x: engine_type == x.engine.type.name, cars))
        return sorted(cars, key=lambda y: y.model)

    def statistics_of_cars(self, attribute: str) -> tuple:
        """
        The method returns statistical data for the size given as an argument.
        Acceptable sizes are price, mileage and engine power.
        The statistics should include the smallest value,
        the highest value and the mean value.
        """
        values = self.get_list_of_values(attribute, self.cars)
        return min(values), round(mean(values), 2), max(values)

    def mileage_sorted_descending(self) -> dict[Car, int]:
        """
        The method returns a dict in which the key is an object of class Car,
        while the value is the number of kilometers that the car has traveled.
        The pairs on the dict are sorted in descending order by value.
        """
        ziped_values = zip(self.cars_obj, self.get_list_of_values('mileage', self.cars))
        return dict(sorted(ziped_values, key=lambda x: x[1], reverse=True))

    def list_of_cars_with_given_tire(self) -> dict[TyreType, list]:
        """
        The method returns a dict where the key is the type of tire (TyreType) and
        the value is a list of cars with this type of tire. The dict is sorted in descending
        order by the number of items in the collection.
        """
        winter_tires, summer_tires = [], []
        for car in self.cars:
            winter_tires.append(car) if car.wheel.type == TyreType.WINTER else summer_tires.append(car)
        dict_ = {TyreType.WINTER: winter_tires, TyreType.SUMMER: summer_tires}
        return dict(sorted(dict_.items(), key=lambda y: len(y[1]), reverse=True))

    def return_cars_that_have_entered_components(self, components: list[str]) -> list[Car]:
        """
        The method returns a collection of cars that have all
        the components from the collection passed as an argument.
        The collection is sorted alphabetically by car model name.
        """
        cars = self.cars.copy()
        return [x for x in cars if set(components).issubset(set(x.car_body.components))]

    @staticmethod
    def get_list_of_values(name: str, list_of_cars) -> list[float | int]:
        """
        Get a list with values for the selected item
        """
        values = []
        for x in list_of_cars:
            if name == 'power':
                values.append(x._asdict()['engine'].power)
            else:
                values.append(x._asdict()[name])
        return values
